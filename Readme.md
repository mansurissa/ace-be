# Notestaker API

## | This is the backend of the **Notestaker**, built with **Django** and **Django REST Framework**. It provides a RESTful API for creating, reading, updating, and deleting notes.

## Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:mansurissa/ace-be.git
cd ace-be
```

### 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run migrations

```
python manage.py runserver
```

---

## API Endpoints

### Base URL: `http://127.0.0.1:8000/api/apps/notes/`

| Endpoint | Method | Description            |
| -------- | ------ | ---------------------- |
| `/`      | GET    | Get all notes          |
| `/`      | POST   | Create a new note      |
| `/{id}/` | GET    | Get a specific note    |
| `/{id}/` | PUT    | Update a specific note |
| `/{id}/` | DELETE | Delete a specific note |
