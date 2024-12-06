Flask CRUD Application:-

This is a simple CRUD (Create, Read, Update, Delete) application built using Flask and SQLite. The app allows users to manage tasks in a list, including the ability to add, edit, and delete tasks.

Table of Contents

Prerequisites

Setup

Project Structure

Features

Running the Application



Prerequisites:

Before running this project, make sure you have the following installed:

Python 3.6+

pip (Python package manager)


Install Dependencies

Install the required Python packages using pip. You can install them by running the following command in your terminal:

pip install -r requirements.txt

The requirements.txt file contains the necessary packages for the project:

Flask
Flask-SQLAlchemy

Setup:

1. Clone the repository to your local machine.

git clone https://github.com/BabuShaik778/flask-crud-app.git

2. Navigate to the project folder:

cd flask-crud-app

3. Install the necessary Python packages (if not done already).

pip install -r requirements.txt

4. The project uses SQLite as the database. The app will automatically create the database (database.db) the first time it runs.


Project Structure:

The project has the following structure:

flask-crud-app/
├── app.py                # Main Flask app file
├── templates/
│   ├── base.html         # Base layout file
│   ├── edit.html         # Edit task page
│   └── index.html        # Task list page
├── static/
│   └── styles.css        # CSS file for styling
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation (this file)

Files Breakdown:

app.py: The main Flask application file, where routes are defined, and the SQLite database is interacted with.

templates/: Contains the HTML files for different pages of the application.

base.html: A base template that other templates extend from.

edit.html: Page for editing an existing task.

index.html: Page that displays the task list and a form to add a new task.


static/: Contains static files like CSS.

styles.css: The styling file for the project.


Features:

Create: Add new tasks to the list.

Read: View the list of tasks with their creation date.

Update: Edit the content of an existing task.

Delete: Remove a task from the list.


Running the Application

To run the Flask app:

1. Navigate to the project directory where app.py is located.

2. Run the Flask application with the following command:

python app.py

By default, the app will run on http://127.0.0.1:5000/. Open this URL in your browser.

Endpoints

GET /: Displays the list of tasks and a form to add new tasks.

POST /: Adds a new task to the database.

GET /edit/<int:id>: Displays the page to edit a task with the given ID.

POST /edit/<int:id>: Updates the task with the provided ID.

GET /delete/<int:id>: Deletes the task with the given ID.


