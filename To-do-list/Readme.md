# Task-Tracker

Task-Tracker is a simple console-based application written in Python. It helps users manage their tasks by providing features such as registration, login, adding tasks, updating task details, and deleting tasks.

## Features

- **Registration**: Users can register themselves by providing a username, password, and security answer.
- **Login**: Registered users can log in using their username and password. If a user forgets their password, they can reset it by providing the correct security answer.
- **Task Management**: Once logged in, users can perform various actions related to task management:
  - View all tasks
  - Add a new task
  - Update task details (name, description, due date, status)
  - Delete tasks

## File Structure

The application utilizes JSON files for storing user account details and task information. Here's a brief overview of the file structure:

- **To-do-list**
  - **accounts**
    - `accounts_detals.json`: JSON file storing user account details (username, password, security answer).
    - `id.txt`: Text file storing unique IDs for tasks.
  - **users_task**
    - `username.json`: JSON files for each registered user, storing their task details.

## Usage

1. **Registration**: Users can register by selecting the "Register Yourself" option and providing the required details.
   - Security Question: Users can set a security question during registration. This question can be used later to reset the password.
2. **Login**: Registered users can log in using their username and password.
   - Forgot Password: If a user forgets their password, they can reset it by answering the security question.
   - Change Password: Users can change their password at any time after logging in.
3. **Task Management**: Once logged in, users can manage their tasks by selecting options such as viewing tasks, adding tasks, updating task details, or deleting tasks.
   - Task Details: Users can view detailed information about each task, including the task name, description, due date, and status.

## Running the Application

To run the Task-Tracker application:

1. Clone the repository to your local machine.
2. Run the `main.py` file To run the program .

## Internship Task

The Task-Tracker application was developed as part of the internship task assigned by CodSoft's project developer, Ahmed Raza. The application uses object-oriented programming concepts and JSON files for data storage.
