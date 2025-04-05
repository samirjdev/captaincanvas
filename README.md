# 📘 Project Setup Guide

This guide will help you set up a virtual environment, install the required libraries, and configure your environment variables.

---

# ✅ Step 1: Create a Virtual Environment

In your project directory, run the following:

```bash
python -m venv venv
```

Activate it like this

- macOS/Linux: `source venv/bin/activate`
- Windows: `venv\Scripts\activate`

# 📦 Step 2: Install Required Libraries

Make sure your virtual environment is activated, then run:

```bash
pip install requests
pip install python-dotenv
```

# 🔐 Step 3: Create Your .env File

In the root of your project, create a file named `.env` with the following content:

`CANVAS_API=INSERT_API_TOKEN_HERE`
