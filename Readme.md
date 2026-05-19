# EMS Backend - Django REST API

A simple Django REST Framework project for learning and practice.

## Setup

### 1. Activate Virtual Environment
```bash
.\myenv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install django djangorestframework
```

### 3. Run Migrations
```bash
cd emsapiproj
python manage.py migrate
```

### 4. Start Development Server
```bash
python manage.py runserver
```

The server will run at `http://127.0.0.1:8000/`

## Project Structure

```
emsapiproj/
├── apibackendapp/          # Main app
│   ├── models.py           # Database models
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views
│   └── urls.py             # App routes
├── emsapiproj/             # Project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Main routes
│   └── wsgi.py             # WSGI config
└── manage.py               # Django CLI
```

## Quick Start

1. Activate virtual environment
2. Run migrations: `python manage.py migrate`
3. Start server: `python manage.py runserver`
4. Visit API endpoints in browser or API client

## Notes

- This is a tutorial practice project
- SQLite database included (db.sqlite3)
- API endpoints defined in `apibackendapp/urls.py`
