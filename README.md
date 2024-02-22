# Django Tasks Manager App

## How to run the project

### First create the virtul env use the following code
To create the virtual env run
- py - m venv <env_name>

After creating the virtual environment run it
-<env_name>\Scripts\activate.bat

You will see the environment name in the command prompt

### Now install django

- pip install django==5.0.2

### Now clone this repository
- git clone https://github.com/RaihanSarkar1/DjangoTask.git

### Now change pointer to project folder
- cd djangotask

### Now install all requirements
- pip install -r requirements.txt

### setup your postgres server according to the settings.py

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