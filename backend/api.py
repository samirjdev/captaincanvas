from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Load the weekly schedule JSON file
def load_weekly_schedule():
    file_path = os.path.join(os.path.dirname(__file__), "weekly_schedule.json")
    with open(file_path, "r") as file:
        return json.load(file)

@app.route("/api/weekly-schedule", methods=["GET"])
def get_weekly_schedule():
    """
    Endpoint to return the contents of weekly_schedule.json.
    """
    try:
        weekly_schedule = load_weekly_schedule()
        return jsonify(weekly_schedule), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)