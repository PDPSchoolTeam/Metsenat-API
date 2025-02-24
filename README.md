# Metsenat-API

![Metsenat-API](https://img.shields.io/badge/Metsenat-API-blue.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/theMirmakhmudov/Metsenat-API)
![GitHub contributors](https://img.shields.io/github/contributors/theMirmakhmudov/Metsenat-API)
![GitHub last commit](https://img.shields.io/github/last-commit/theMirmakhmudov/Metsenat-API)



Metsenat-API is a RESTful API designed for managing sponsorships and donations, facilitating transparent interactions between donors and recipients.

## 📌 Features
- User authentication and authorization
- Sponsor and student management
- Donation tracking and reporting
- Secure and optimized API endpoints

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- PostgreSQL (or any preferred database)
- Docker (optional but recommended)

### Installation (Windows, Linux, Mac)
1. Clone the repository:
   ```sh
   git clone https://github.com/theMirmakhmudov/Metsenat-API.git
   cd Metsenat-API
   ```

2. Create a virtual environment:
   - **Windows**
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Mac/Linux**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update database and secret key values accordingly

### Database Migration
Run the following commands to set up the database:
```sh
python manage.py makemigrations
python manage.py migrate
```

```sh
make mig
```

### Running the Server
- **Windows, Mac, Linux:**
  ```sh
  python manage.py runserver
  ```

  ```sh
  make run
  ```

  
  

## 📂 Project Structure
```
Metsenat-API/
│── manage.py           # Django management script
│── .env.example        # Environment variables example
│── requirements.txt    # Python dependencies
│── Dockerfile          # Docker configuration
│── docker-compose.yml  # Docker Compose setup
│── config/             # Project configuration files
│   ├── settings.py     # Django settings
│   ├── urls.py         # URL routing
│── api/                # Main API application
│   ├── admin.py        # Admin configuration
│   ├── apps.py         # App configuration
│   ├── managers.py     # Custom model managers
│   ├── models.py       # Database models
│   ├── serializers.py  # API serializers
│   ├── tests.py        # Unit tests
│   ├── urls.py         # API routes
│   ├── views.py        # API views
│── docs/               # API documentation
│── media/              # Uploaded media files
│   ├── avatar/
│       ├── student/
│           ├── default-student.webp
│── Metsenat/           # Core project settings
│   ├── asgi.py         # ASGI configuration
│   ├── settings.py     # Project settings
│   ├── urls.py         # Root URL configuration
│   ├── wsgi.py         # WSGI configuration
│── LICENSE             # Project license
│── README.md           # Project documentation
│── Makefile            # Automation scripts
```

## 🛠 API Endpoints
| Method | Endpoint                  | Description          |
|--------|---------------------------|----------------------|
| GET    | `/api/sponsors/`          | List sponsors       |
| POST   | `/api/sponsors/`          | Create a sponsor    |
| GET    | `/api/students/`          | List students       |
| POST   | `/api/students/`          | Register a student  |

📖 Full API documentation is available via Swagger UI at:
```sh
http://localhost:8000/api/docs/
```

## 🏗 Deployment

### Docker Setup (Optional)
1. Build and run the container:
   ```sh
   docker-compose up --build -d
   ```
2. Run database migrations:
   ```sh
   docker-compose exec web python manage.py migrate
   ```

### Gunicorn & Nginx (Production)
- Use Gunicorn for running the Django application.
- Set up Nginx as a reverse proxy for handling requests efficiently.

## 🛡 Security Best Practices
- Store sensitive credentials in environment variables.
- Use Django's built-in security middleware.
- Regularly update dependencies.

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit changes.
4. Submit a pull request.

## 📜 License
This project is licensed under the MIT License.

## 📬 Contact
- **Author:** [theMirmakhmudov](https://github.com/theMirmakhmudov)
- **Email:** mr.mirmakhmudov16112008@gmail.com

---

Enjoy using **Metsenat-API**! 🎉

