# Django Tasks Manager App (under development)

## Upcoming Features
1. UI changes and fixes
2. User login, account and feature
3. Rest API feature

## Features

1. Create Task add multiple images and due date
2. View All Tasks
3. Delete or Edit and existing task
4. View details of a task
5. Set priority of a task

## How to run the project

### Prequisites to install
1. python
2. postgresSQL

### First create the virtul env use the following code
To create the virtual env run this in the project folder
- py - m venv <env_name>

After creating the virtual environment activate the virtual environment
- <env_name>\Scripts\activate

You will see the environment name in the command prompt

### Now clone this repository
- git clone https://github.com/RaihanSarkar1/DjangoTask.git

### Now change pointer to project folder
- cd djangotask

### Now install all requirements
- pip install -r requirements.txt

### Setup your postgres server according to the settings.py

### Run migrations
- py manage.py makemigrations
- py manage.py migrate

### All set now run the server
- py manage.py runserver


# Rest API Usage

To access and list all tasks in the tasks app the url is:
* api/list

To create a task the url is:
* api/create

