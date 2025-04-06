import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
from dotenv import load_dotenv
import json  # Import JSON module to write data to a file

# Load the API token from .env file
load_dotenv()
API_TOKEN = os.getenv("CANVAS_API")
BASE_URL = "https://usflearn.instructure.com/api/v1"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

class Assignment:
    """Class to represent an assignment."""
    def __init__(self, name, due_date, description):
        self.name = name
        self.due_date = due_date
        self.description = description

    def to_dict(self):
        """Convert the assignment to a dictionary."""
        return {
            "name": self.name,
            "due_date": self.due_date,
            "description": self.description
        }

class Course:
    """Class to represent a course."""
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.assignments = []

    def add_assignment(self, assignment):
        """Add an assignment to the course."""
        self.assignments.append(assignment)

    def to_dict(self):
        """Convert the course to a dictionary."""
        return {
            "name": self.name,
            "assignments": [assignment.to_dict() for assignment in self.assignments]
        }

def fetch_all_pages(url):
    """Fetch all pages of results from a paginated Canvas API endpoint."""
    results = []
    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        results.extend(response.json())

        # Get the 'next' link from the Link header
        link_header = response.headers.get("Link", "")
        next_url = None
        if link_header:
            links = link_header.split(",")
            for link in links:
                if 'rel="next"' in link:
                    next_url = link[link.find("<") + 1 : link.find(">")]
                    break
        url = next_url  # Update the URL to the next page
    return results

def get_favorited_courses():
    """Fetch all favorited courses."""
    url = f"{BASE_URL}/users/self/favorites/courses"
    return fetch_all_pages(url)

def get_assignments_for_course(course_id):
    """Fetch all assignments for a specific course."""
    url = f"{BASE_URL}/courses/{course_id}/assignments"
    return fetch_all_pages(url)

def clean_html(html_content):
    """Extract plain text from HTML content and remove excessive new lines."""
    if not html_content:  # Handle None or empty content
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n").strip()
    # Remove excessive new lines and extra spaces
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())

def extract_description(assignment):
    """Extract and clean the description for an assignment."""
    description_html = assignment.get("description", "")
    return clean_html(description_html)

def main():
    # Get today's date
    today = date.today()

    # Dictionary to store courses and their assignments
    courses_data = {}

    # Get favorited courses
    courses = get_favorited_courses()
    for course in courses:
        course_id = course["id"]
        course_name = course["name"]
        course_end_date = course.get("end_at")

        # Skip courses without an end date or already ended
        if course_end_date:
            course_end_date = datetime.strptime(course_end_date, "%Y-%m-%dT%H:%M:%SZ").date()
            if course_end_date < today:
                continue

        # Create a Course object
        course_obj = Course(course_id, course_name)

        # Get assignments for the course
        assignments = get_assignments_for_course(course_id)
        for assignment in assignments:
            due_date = assignment.get("due_at")
            if due_date:  # Only process assignments with a due date
                due_date = datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%SZ").date()
                if due_date >= today:  # Only include assignments due today or in the future
                    description = extract_description(assignment)
                    assignment_obj = Assignment(assignment["name"], str(due_date), description)
                    course_obj.add_assignment(assignment_obj)

        # Only add the course to the dictionary if it has assignments
        if course_obj.assignments:
            courses_data[course_id] = course_obj.to_dict()

    # Write the data to a JSON file
    with open("courses_data.json", "w") as json_file:
        json.dump(courses_data, json_file, indent=4)

    print("Data has been written to courses_data.json")

if __name__ == "__main__":
    main()