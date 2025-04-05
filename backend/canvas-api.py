import requests

# Replace these with your Canvas API details
API_URL = "https://usflearn.instructure.com/api/v1"
API_TOKEN = "13~K4rG8W44ear3nBVz787uAkrQGfFFDc9XrAEAUu3Gmx2ERNxeNQGX4Hz4tBFaC6UV"

def get_favorited_courses():
    """
    Fetches the list of favorited courses for the user, handling pagination.
    """
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    url = f"{API_URL}/courses?enrollment_state=active&include[]=favorites"
    all_courses = []

    while url:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            courses = response.json()
            all_courses.extend(courses)

            # Check for the 'next' link in the response headers
            links = response.headers.get('Link', '')
            next_url = None
            for link in links.split(','):
                if 'rel="next"' in link:
                    next_url = link[link.find('<') + 1:link.find('>')]
                    break
            url = next_url  # Update the URL to the next page
        else:
            print(f"Failed to fetch courses. Status code: {response.status_code}, Response: {response.text}")
            return

    # Filter and display only favorited courses
    for course in all_courses:
        if course.get('is_favorite', False):
            course_id = course.get('id', 'N/A')
            course_name = course.get('name', 'Unnamed Course')
            print(f"Course ID: {course_id}, Name: {course_name}")

if __name__ == "__main__":
    get_favorited_courses()