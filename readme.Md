# Notes Taking APIs

## List of APIs
1. Create Notes
2. List All Notes
3. Fetch One Note using Pk
4. Search Notes through titles in query params
5. update notes

## Additional Features
1. Included Test Cases for all APIs using Pytest
2. Attached Swagger for API Docs
3. Used generic views for writing all the APIs 

## Steps to run this project 
1. Clone this repository  [Repo Link]([prafullpandey614/Notes-APP-Crud-API (github.com)](https://github.com/prafullpandey614/Notes-APP-Crud-API))
2. Create Virtual Environment
   ``` bash
   python -m venv env
   env\Scripts\activate
   ```
3.  Install Dependencies
	```
	pip install -r requirements.txt
	```
4. Run Migrations
	```
	python manage.py makemigrations
	python manage.py migrate
	```
5. Start the server
	```
	python manage.py runserver
	```
6. Get Swagger Docs on this endpoint http://127.0.0.1:8000/swagger/
	
 