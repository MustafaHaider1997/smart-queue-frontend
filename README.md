# 🖥️ Smart Queue – Frontend (Flask UI)

The **Smart Queue Frontend** is a simple, interactive **Flask-based web UI** for patients to register, log in, view, book, update, and cancel appointments. It interacts with the underlying **User** and **Appointment** microservices using REST APIs and secures access via JWT tokens.

---

## 🎯 Features

* 🔐 User registration and login (via User Service)
* 📅 View all appointments
* ➕ Create a new appointment
* ✏️ Update existing appointments
* ❌ Delete/cancel appointments
* 💻 Responsive Bootstrap-based UI
* 🔒 JWT-based authentication stored in session
* 🐳 Dockerized and orchestratable via Docker Compose

---

## 🛠️ Tech Stack

| Component           | Technology               |
| ------------------- | ------------------------ |
| **Language**        | Python 3.12              |
| **Framework**       | Flask                    |
| **Frontend UI**     | HTML5, CSS3, Bootstrap 5 |
| **API Integration** | requests, JWT            |
| **Deployment**      | Docker, Docker Compose   |

---

## 📁 Project Structure

```
smart-queue-frontend/
├── app.py                 # Flask application with all routes
├── templates/             # HTML UI templates (Jinja2)
│   ├── index.html         # Home page
│   ├── layout.html        # Common base layout
│   ├── login.html         # Login form
│   ├── register.html      # Registration form
│   └── appointments.html  # Appointment dashboard
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker setup
└── venv/                  # Virtual environment (ignored in container)
```

---

## 🌐 Environment Configuration

Create a `.env` file (not needed in container if using Docker Compose):

```env
USER_API_URL=http://user-service:8000/api/v1/users
APPT_API_URL=http://appointment-service:80/api/v1/appointments
```

When running locally, update `USER_API_URL` and `APPT_API_URL` accordingly:

```env
USER_API_URL=http://localhost:8000/api/v1/users
APPT_API_URL=http://localhost:5243/api/v1/appointments
```

---

## ▶️ Running the Frontend

### Locally

```bash
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port=3001
```

Then visit: [http://localhost:3001](http://localhost:3001)

---

## 🐳 Docker Instructions

### Build & Run with Docker

```bash
docker build -t smart-queue-frontend .
docker run -p 3001:3001 --env-file .env smart-queue-frontend
```

Or via Docker Compose:

```yaml
frontend:
  build: ./smart-queue-frontend
  ports:
    - "3001:3001"
  depends_on:
    - user-service
    - appointment-service
```

---

## 🔑 Login and JWT Flow

* Login sends `POST /login` to the **User Service**
* Stores JWT token in session
* Adds `Authorization: Bearer <token>` to every appointment-related API call

---

## 💡 UI Preview

| Page          | Description                        |
| ------------- | ---------------------------------- |
| **Home**      | Landing page with options          |
| **Register**  | Create new user account            |
| **Login**     | User login and token storage       |
| **Dashboard** | List, create, update, delete appts |

---

## 🔄 Integration Flow

* **User Service** handles registration and login
* **Appointment Service** handles appointment CRUD
* **Frontend** consumes both services via REST APIs

---

## 🔐 Security

* JWT token-based session
* Token validation on backend via secure headers
* Role-based checks possible if needed (future)

---

## 📄 License

This project is licensed under the MIT License.
