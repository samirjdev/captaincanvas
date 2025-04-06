
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
        [f"- {assignment['name']}: {assignment['description']}" for assignment in assignments]
    )
    course_descriptions.append(f"Course: {course_name}\nAssignments:\n{assignment_descriptions}")

prompt = (
    "Here is a list of courses with their assignments and descriptions. "
    "Please score each assignment by difficulty on a scale of 1 to 10, where 1 is the easiest and 10 is the hardest, "
    "relative to the other assignments across all courses. Provide the scores in JSON format, "
    "with the course names as keys and the assignments as a list of objects containing the assignment name and its difficulty score.\n\n"
    "PLEASE DO NOT OUTPUT ANYTHING ELSE EXCEPT FOR THE JSON OUTPUT"
    + "\n\n".join(course_descriptions)
)

# print(prompt)

response = client.responses.create(
    model="gpt-4o-mini-2024-07-18",
    input=prompt
)

print(response.output_text)