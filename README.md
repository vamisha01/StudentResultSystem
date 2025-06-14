# Student Result Management System 🎓

A full-stack web application to manage student results, built with **Django** (backend) and **PostgreSQL** database. Provides REST APIs for managing students, subjects, marks, and calculating results.

## ✅ Features
- CRUD operations for Students, Subjects, Marks
- Generate total marks, percentage, and grade
- REST API with Django REST Framework
- PostgreSQL for database
- Admin panel for management

## 🚀 Tech Stack
- Backend: Django, Django REST Framework
- Database: PostgreSQL
- Environment Variables: python-decouple

## 🗂️ API Endpoints

| Endpoint            | Method | Description                |
| ------------------- | ------ | -------------------------- |
| `/api/students/`    | GET/POST/PUT/DELETE | Manage students     |
| `/api/subjects/`    | GET/POST/PUT/DELETE | Manage subjects     |
| `/api/marks/`       | GET/POST/PUT/DELETE | Add/view marks      |
| `/api/results/`     | GET/POST/PUT/DELETE | View results        |

## 🛠️ Setup Instructions

```bash
git clone https://github.com/your-username/student-result-system.git
cd student-result-system
python -m venv env
source env/bin/activate   # For Windows: env\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
