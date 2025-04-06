from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import schedule
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the weekly schedule JSON file
def load_weekly_schedule(api_key):
    # Ensure the schedule is generated before loading
    schedule.generate_weekly_schedule(api_key)
    file_path = os.path.join(os.path.dirname(__file__), "weekly_schedule.json")
    with open(file_path, "r") as file:
        return json.load(file)

@app.route("/", methods=["GET"])
def root():
    """Root endpoint to indicate the server is running."""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Server Status</title>
    </head>
    <body>
        <h1>The server is up and running!</h1>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/api/weekly-schedule", methods=["GET"])
def get_weekly_schedule():
    try:
        # Get the Canvas API key from the query parameter or header
        api_key = request.args.get("api_key") or request.headers.get("Authorization")
        if not api_key:
            return jsonify({"error": "Canvas API key is required"}), 400

        # Load the weekly schedule using the provided API key
        weekly_schedule = load_weekly_schedule(api_key)
        return jsonify(weekly_schedule), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)