# Metsenat-API

> Django RESTful API for managing sponsorships and donations for students and universities.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Metsenat-API is a Django-based RESTful API that facilitates the management of sponsorships and donations, enabling seamless connections between sponsors, students, and universities.

## Features
- CRUD operations for Universities, Students, Sponsors, and Donations.
- Secure authentication and authorization.
- Detailed donation tracking and management.
- Scalability with Django and Django REST Framework.

## Technologies Used
- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- Docker (for containerization)

## Installation

### Prerequisites
- Python 3.12
- PostgreSQL
- Docker (optional)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/theMirmakhmudov/Metsenat-API.git
   cd Metsenat-API
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage
Access the API at `http://127.0.0.1:8000/` using tools like [Postman](https://www.postman.com/).

## API Endpoints
- **Universities:** `/api/universities/`
- **Students:** `/api/students/`
- **Sponsors:** `/api/sponsors/`
- **Donations:** `/api/donations/`

## Project Structure
- `manage.py` – Django management script
- `metsenat/` – Main project folder
- `api/` – API app containing models, serializers, views, and urls

## Contributing
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

