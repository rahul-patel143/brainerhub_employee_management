# Django Employee Management API

## 🚀 Project Overview
This project is a Django-based REST API that allows users to:
- Upload an Excel/CSV file to insert employee data into a PostgreSQL database.
- Retrieve all employees or a specific employee by ID.
- Store company details and associate employees with a company.
- Use Swagger API documentation for easy testing.

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Libraries**: Pandas (for Excel/CSV processing), DRF-YASG (Swagger API docs)
- **Tools**: Docker (optional for database setup), Virtual Environment

---

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd <project-folder>
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL Database
- Create a PostgreSQL database and update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'brainerhub_emp_management',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
The API will be accessible at: `http://127.0.0.1:8000/`

### 7️⃣ Access Swagger API Docs
Swagger UI for API testing is available at:
```bash
http://127.0.0.1:8000/api/docs
```

---

## 📂 API Endpoints

### 🔹 Upload Employee Data (Excel/CSV)
**Endpoint:** `POST /api/upload/`
- **Description:** Uploads an Excel/CSV file and inserts data into the database.
- **Request:** Multipart file upload (`file` parameter).
- **Response:**
```json
{
    "message": "Data uploaded successfully"
}
```

### 🔹 Get All Employees
**Endpoint:** `GET /api/employees/`
- **Description:** Fetches all employees with their associated company name.
- **Response:**
```json
[
    {
        "id": 1,
        "employee_id": 198,
        "first_name": "Donald",
        "last_name": "OConnell",
        "phone_number": "650.507.9833",
        "salary": 2600.00,
        "manager_id": 100,
        "department_id": 1,
        "company_name": "SH_CLERK"
    }
]
```

### 🔹 Get a Specific Employee
**Endpoint:** `GET /api/employees/{id}/`
- **Description:** Fetches details of a specific employee by ID.
- **Response:**
```json
{
    "id": 1,
    "employee_id": 198,
    "first_name": "Donald",
    "last_name": "OConnell",
    "phone_number": "650.507.9833",
    "salary": 2600.00,
    "manager_id": 100,
    "department_id": 1,
    "company_name": "SH_CLERK"
}
```

---

## 🏗️ Project Structure
```
📂 employee_api/
├── 📂 employees/  # Employee management app
│   ├── models.py  # Database models
│   ├── views.py  # API views
│   ├── serializers.py  # DRF serializers
│   ├── urls.py  # API routes
├── 📂 core/  # Project settings
│   ├── settings.py  # Django settings
│   ├── urls.py  # Project URLs
├── manage.py  # Django management script
```

---

## 🔥 Additional Features
- **Data Validation:** Ensures required fields are present during upload.
- **Optimized Queries:** Uses `.select_related('company')` to fetch related data efficiently.
- **Swagger Documentation:** Provides an interactive API testing interface.

---

## 📝 Future Enhancements
- Add JWT authentication for secure API access.
- Implement role-based access control (RBAC).
- Support file uploads from cloud storage (e.g., AWS S3).
- For Big files upload create socket for stable connection.

---

## 📌 Author
Developed by **Rahul Patel**

