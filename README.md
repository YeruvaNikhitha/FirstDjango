# Django Student CRUD App

This is a simple web application built using Django.  
The project demonstrates basic CRUD operations (Create, Read, Update, Delete).

## Features

- Add new student
- View student list
- Update student details
- Delete student records
- Simple UI using HTML and Bootstrap

## Tech Stack

- Python
- Django
- SQLite
- HTML
- Bootstrap

## Project Structure

studentproject/
│
├── manage.py
├── studentproject/
│   ├── settings.py
│   ├── urls.py
│
└── students/
    ├── models.py
    ├── views.py
    ├── templates/
        ├── list.html
        ├── add.html
        ├── edit.html


## How to Run the Project

1. Clone the repository

git clone https://github.com/yourusername/FirstDjango.git


2. Go into the project folder

cd FirstDjango


3. Install dependencies

pip install django


4. Run migrations

python manage.py migrate


5. Start the server

python manage.py runserver


6. Open in browser

http://127.0.0.1:8000


## Author

Nikhitha Reddy
