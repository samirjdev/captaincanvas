# 🚀 Captain Canvas: An AI-Powered Canvas Course Charter and Navigator

Captain Canvas is a productivity tool specifically designed to streamline and enhance students' interactions with the Canvas Learning Management System (LMS). By leveraging the Canvas API alongside advanced AI capabilities, Captain Canvas automates the retrieval of course data, assignments, and deadlines directly from Canvas, presenting them in a clear, actionable format.

Whether you're managing a heavy course load or tackling last-minute deadlines, Captain Canvas helps reduce stress, stay organized, and maximize your academic performance.

### Challenges We Ran Into

We ran into numerous difficult challenges as our track and challenges changed during the hackathon. We changed our project idea three times which lost us well over five hours after the hackathon began. With our limited time, we ran into major issues trying to connect our API to the front end.

### Accomplishments We Are Proud Of

We're proud to have produced a completed project given the major complications we ran into. Despite the time troubles and numerous errors, we encountered early into the morning, we were able to keep at it and not lose hope.

### What We Learned From This Experience

HackUSF taught us how to use and incorporate Angular into our front end. We used lessons learned from our previous hackathons to better handle the time pressure we encountered this time.

---

## 🎯 Key Features

- **Personalized Weekly Schedule:** Instantly generates a custom weekly schedule to equip you with individualized study plans.
- **Cram Mode:** Prioritize assignments due within the next 24 hours, helping you manage urgent tasks effectively.
- **AI Summaries & Difficulty Ratings:** Automatically summarizes assignment details and provides difficulty ratings to clearly illustrate your workload.
- **Seamless Integration:** Combines Angular for a responsive and intuitive front-end experience and Flask for a strong backend on any mobile or web device.

---

## 🛠️ Tech Stack

- **Front-end:** Angular
- **Backend:** Flask
- **AI Integration:** OpenAI
- **Libraries:** BeautifulSoup4, python-dotenv

---

## 📘 Installation & Setup Guide

Follow these steps to set up and run Captain Canvas:

### ✅ Step 1: Clone Repository
Clone the repository to your local machine:
```bash
git clone <repository-url>
cd <repository-folder>
```

### 🐍 Step 2: Create a Virtual Environment
Create and activate a Python virtual environment to keep your dependencies organized:

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 📦 Step 3: Install Required Libraries
With your virtual environment activated, run:
```bash
pip install requests bs4 python-dotenv openai
```

### 🔐 Step 4: Configure Environment Variables
Create a `.env` file at the root of your project directory and add your Canvas API key and OpenAI API key:

```dotenv
CANVAS_API=YOUR_CANVAS_API_TOKEN
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Replace `YOUR_CANVAS_API_TOKEN` and `YOUR_OPENAI_API_KEY` with your actual API tokens.

---

## 🚦 Running the Application
After setting up the environment and installing the libraries, you can run the Flask backend:

```bash
python app.py
```

Then, start your Angular front-end application:

```bash
cd frontend
npm install
npm start
```

Your application should now be running and accessible from `http://localhost:4200`.

---

Happy studying with Captain Canvas! 📚✨
