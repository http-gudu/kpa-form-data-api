# 🚄 KPA Form Data API

A FastAPI backend service for managing **bogie checksheets** and **wheel specifications** as part of railway maintenance and inspection workflows.

This project is built using **FastAPI**, uses **MongoDB Atlas** for data storage, and includes clean API design, validation, and auto-generated documentation.

---

## ✅ Features

- 🔧 **MongoDB Atlas Integration** using `motor` (async driver)
- 📄 **Bogie Checksheet API** – create and manage bogie inspections
- ⚙️ **Wheel Specification API** – add and filter wheel data with pagination
- 🛡 **Validation** – input validation with Pydantic schemas
- 🌐 **Auto Docs** – Swagger UI (`/docs`) and Redoc (`/redoc`)
- 💡 **RESTful API** – uses proper status codes and clear endpoints

---

## 📦 Technology Stack

| Tool/Library     | Purpose                          |
|------------------|----------------------------------|
| FastAPI          | Web API Framework (async)        |
| Motor            | MongoDB Driver (async)           |
| Pydantic         | Data validation                  |
| Python Dotenv    | Environment variable management  |
| Uvicorn          | ASGI server                      |

---

## 🔐 Setup Instructions

###1. Clone the repository

```bash
git clone https://github.com/yourname/kpa-form-api.git
cd kpa-form-api
###2. Setup virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure .env file
env
Copy
Edit
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/kpa_db?retryWrites=true&w=majority
5. Run the server
bash
Copy
Edit
uvicorn app.main:app --reload
Visit:

Swagger Docs → http://localhost:8000/docs

ReDoc UI → http://localhost:8000/redoc