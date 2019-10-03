# API with Flask to create a TODOs list

## Context

An **Angular.js** Todo application was provided with the basic **Create, Read, Update, Delete (CRUD)** functionalities to generate a TODO list. This application used the ng-resource plugin which allows the application to work automatically using RESTful practices.

The aim of this project was to **provide a back-end** solution for a client-side app usign API RESTful flask.

## Project details

* The API is versioned and all routes are prefixed with **/api/v1**

* When the app starts it will fetch all Todos in the system usign a **GET request**.

* When a Todo is created and the save link is double-clicked, it will make a **POST request** to the server. 

* When a previously saved Todo is updated and the save link is double-clicked, it will make a **PUT request** to the server.

* When a previously saved Todo is deleted and the save link is double-clicked, it will make a **DELETE request** to the server. 

* Unit tests were written to test views is displaying the correct information and that models, classes, and other functions behave as expected.

* PEP8 style was verified using the utility **flake8**

## Test the App in terminal

1. Download the repository and install the requirements.
		
		pipenv install
		pipenv shell
		pip install -r requirements.txt
		

2. Run the application.
		
		python3 app.py

3. Open your favorite web browser and type:

		http://localhost:8000/


Enjoy! :shipit: