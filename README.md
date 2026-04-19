# Flask API Service

A simple Flask-based REST API project built to learn backend development, testing, and CI/CD fundamentals using GitHub Actions.

---

## 🚀 Features

- Flask REST API
- Basic endpoints:
  - `/` → Health check
  - `/status` → Service status
  - `/add/<a>/<b>` → Simple addition operation
- Automated testing using pytest
- Continuous Integration (CI) using GitHub Actions
- Environment variable support

---

## 🧰 Tech Stack

- Python
- Flask
- Pytest
- Git & GitHub
- GitHub Actions (CI)

---

## 📁 Project Structure

flask-api/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_app.py

---

## ▶️ How to Run Locally

1. Clone the repo:
git clone https://github.com/<your-username>/flask-api.git
cd flask-api

2. Create virtual environment:
python -m venv venv

Mac/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
python app.py

App runs at:
http://127.0.0.1:5000

---

## 🧪 Run Tests

pytest

---

## ⚙️ CI/CD Pipeline

This project uses GitHub Actions to:

- Install dependencies
- Run tests automatically
- Validate code on every push to main

Check it under the GitHub “Actions” tab.

---

## 📌 Future Improvements

- Add Docker support
- Add database integration (SQLite/PostgreSQL)
- Expand API into full CRUD service
- Deploy to cloud (AWS / Render / Railway)
