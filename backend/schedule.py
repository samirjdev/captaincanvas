
from openai import OpenAI
from dotenv import load_dotenv
import os
import assignments as assigns
import json

def generate_weekly_schedule(api_key):
    assigns.retrieve_canvas_data(api_key)  # Generate the courses_data.json file

    # Set your OpenAI API key
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")

    # Load the course data from the JSON file
    with open("courses_data.json", "r") as json_file:
        courses_data = json.load(json_file)

    # Prepare the prompt for ChatGPT
    course_descriptions = []
    for course_id, course_info in courses_data.items():
        course_name = course_info["name"]
        assignments = course_info["assignments"]
        assignment_descriptions = "\n".join(
            [f"- {assignment['name']} (Due: {assignment['due_date']}): {assignment['description']}" for assignment in assignments]
        )
        course_descriptions.append(
            f"Course ID: {course_id}\nCourse Name: {course_name}\nAssignments:\n{assignment_descriptions}"
        )

    prompt = (
        "Here is a list of courses with their assignments and descriptions. "
        "Assigments can be due more than a week in advance, just make sure to balance out the difficulty."
        "For example, a project can be due 3 weeks, but you can assign it near the ned of the current week."
        "However, if you notice assignments that are named similar: e.g. PS-5, PS-6 those are probably weekly assignmnets (look at due date to verify)"
        "so you need to space those out more evenly"
        "If its managable, you can include all classes given to you. Minimum of one assignment must be given each day"
        "If you decide to not include a specific assignment, please exclude it from the final json prompt."
        "Please create a weekly schedule by assigning one or more assignments to each day of the week (0 = Sunday, 1 = Monday, ..., 6 = Saturday). "
        "Balance higher difficulty assignments with lower difficulty ones to make the schedule manageable. "
        "If there are more assignments than days in the week, you can assign multiple assignments to the same day. "
        "Ensure the assignments are added in the proper order based on their due dates or logical progression. "
        "Do not include assignments that are empty or missing descriptions. "
        "For each assignment, provide the day it should be worked on, its difficulty score 1 through 5, and its due date. "
        "Provide the results in JSON format, with the course IDs as keys. Each course should include the course name and a list of assignments, "
        "where each assignment has its name, difficulty score, due date, and assigned day.\n\n"
        "PLEASE DO NOT RETURN ASSIGNMENTS THAT ARE EMPTY OR EMPTY LIST."
        "PLEASE DO NOT OUTPUT ANYTHING ELSE EXCEPT FOR THE JSON OUTPUT, DO NOT PUT IN A MARKDOWN CELL, DO NOT ADD NEW LINES, JUST RAW CLEAN JSON THAT CAN BE JSONIFIED\n\n"
        + "\n\n".join(course_descriptions)
    )

    response = client.responses.create(
        model="gpt-4o-mini-2024-07-18",
        input=prompt
    )

    

    # Assuming `response.output_text` contains the pure JSON string
    response_text = response.output_text

    # Parse the JSON content
    try:
        result_json = json.loads(response_text)  # Convert the JSON string to a Python dictionary

        # Write the parsed JSON to a new file
        with open("weekly_schedule.json", "w") as output_file:
            json.dump(result_json, output_file, indent=4)  # Write the JSON with indentation for readability

        print("The weekly schedule has been written to 'weekly_schedule.json'.")

        # Load the course data JSON file
        with open("courses_data.json", "r") as course_data_file:
            course_data = json.load(course_data_file)

        # Update the JSON with links from the course data
        for course_id, course_info in result_json.items():
            # Add the course link if it exists in the course data
            if course_id in course_data:
                course_info["link"] = course_data[course_id].get("link", "")

                # Iterate through all assignments and match by name
                for assignment in course_info.get("assignments", []):
                    # Match assignments by name and add the link
                    for original_assignment in course_data[course_id].get("assignments", []):
                        # Use a case-insensitive comparison and strip extra spaces
                        if assignment["name"].strip().lower() == original_assignment["name"].strip().lower():
                            assignment["assignment_link"] = original_assignment.get("assignment_link", "")
                            break  # Exit the loop once a match is found

        # Write the updated JSON to a new file
        with open("weekly_schedule.json", "w") as updated_output_file:
            json.dump(result_json, updated_output_file, indent=4)

        print("The updated weekly schedule with links has been written to 'weekly_schedule.json'.")

    except json.JSONDecodeError as e:
        print("Failed to parse JSON from ChatGPT response:", e)
        print("Raw response text:", response_text)


    # Load the original JSON file
    with open("weekly_schedule.json", "r") as file:
        data = json.load(file)

    # Create a new structure for the reordered JSON
    reordered_data = []

    # Iterate through the courses and assignments
    for course_id, course_info in data.items():
        course_name = course_info["course_name"]
        course_link = course_info["link"]
        assignments = course_info["assignments"]

        for assignment in assignments:
            assigned_day = assignment["assigned_day"]

            # Ensure the list has enough indices for the assigned day
            while len(reordered_data) <= assigned_day:
                reordered_data.append([])

            # Add the assignment info to the corresponding day
            reordered_data[assigned_day].append({
                "course_name": course_name,
                "course_link": course_link,
                "assignment": {
                    "name": assignment["name"],
                    "difficulty_score": assignment["difficulty_score"],
                    "due_date": assignment["due_date"],
                    "assignment_link": assignment["assignment_link"]
                }
            })

    # Save the reordered JSON to a new file
    with open("weekly_schedule.json", "w") as file:
        json.dump(reordered_data, file, indent=4)

    print("Reordered JSON has been saved to 'weekly_schedule.json'.")

# generate_weekly_schedule(os.getenv("CANVAS_API_KEY"))