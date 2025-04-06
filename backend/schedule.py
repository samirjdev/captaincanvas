
from openai import OpenAI
from dotenv import load_dotenv
import json
import os

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
    "For each assignment, provide the day it should be worked on, its difficulty score, and its due date. "
    "Provide the results in JSON format, with the course IDs as keys. Each course should include the course name and a list of assignments, "
    "where each assignment has its name, difficulty score, due date, and assigned day.\n\n"
    "PLEASE DO NOT OUTPUT ANYTHING ELSE EXCEPT FOR THE JSON OUTPUT\n\n"
    + "\n\n".join(course_descriptions)
)

response = client.responses.create(
    model="gpt-4o-mini-2024-07-18",
    input=prompt
)

print(response.output_text)