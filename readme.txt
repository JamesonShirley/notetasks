Superuser
Username: group
Password: Password

important urls: 
http://127.0.0.1:8000/notetasks/notes/
http://127.0.0.1:8000/notetasks/tasks/
http://127.0.0.1:8000/notetasks/tasks/calendar/
http://127.0.0.1:8000/admin/



# Django Project Setup and Installation Guide

Welcome to the Django project! This README will guide you through the process of setting up and running the Django application on your local environment.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Server](#running-the-server)
- [Accessing the App](#accessing-the-app)
- [Creating a Superuser](#creating-a-superuser)
- [Additional Notes](#additional-notes)

## Prerequisites
Before setting up the project, ensure you have the following installed on your system:
- Python (version 3.6 or later)
- Git (for cloning the project repository)
- A virtual environment tool (such as `venv` or `virtualenv`)

## Installation
1. **Clone the Repository**
   - Use Git to clone the repository to your local machine:
     ```bash
     git clone <repository_url>
     cd <repository_name>
     ```

2. **Create a Virtual Environment**
   - Create a virtual environment in the project directory:
     ```bash
     python -m venv venv
     ```

3. **Activate the Virtual Environment**
   - Activate the virtual environment to ensure packages are installed in an isolated environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**
   - With the virtual environment activated, install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

## Database Setup
1. **Configure Database Settings**
   - Modify the `settings.py` file in your Django project to configure your database connection. If you're using SQLite (the default), this step is not required.

2. **Run Migrations**
   - Apply the database migrations to set up the database schema:
     ```bash
     python manage.py migrate
     ```

## Running the Server
1. **Start the Django Development Server**
   - With the virtual environment activated and migrations applied, start the Django development server:
     ```bash
     python manage.py runserver
     ```

2. **Access the Application**
   - Open a web browser and navigate to `http://127.0.0.1:8000/` to view the Django app.

## Creating a Superuser
To access the Django admin site, you need a superuser account. Here's how to create one:
1. **Create a Superuser**
   - Run the following command and follow the prompts to create a superuser:
     ```bash
     python manage.py createsuperuser
     ```

2. **Access the Admin Site**
   - After creating a superuser, navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

## Additional Notes
- **Deactivating the Virtual Environment**
  - To exit the virtual environment, use the following command:
    ```bash
    deactivate
    ```

- **Common Commands**
  - Run tests: `python manage.py test`
  - Check Django version: `python manage.py version`
  - Create a new Django app: `python manage.py startapp <app_name>`

If you encounter any issues during setup or require further assistance, please contact the project maintainer or raise an issue in the project's repository.
