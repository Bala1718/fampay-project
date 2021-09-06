# Fampay-Project

This Project is written in Python with Django Framework.
The main idea is to fetch Youtube videos every 15 seconds after 1st March, 2020.

# Django-Project Architecture

Django follows Model View Template Architecture/ Model View Controller Part. It has three segments into it, Model, Views, Controller / Model, Views, Template.

<img width="323" alt="Screenshot 2021-09-06 at 7 43 02 PM" src="https://user-images.githubusercontent.com/19856958/132230163-1b575ea0-4bf4-4db4-8508-0496acab6139.png">

# Model

A Model is an python class which contains Business logic in Django Architecture. It's acts as an Mediator between the web interface and the DataBase.

# View

Views interacts with Model to execute the Business Logic written in Model. The view fetches data from Model. It gives Template Access Specific data to be displayed.

# Template

It's user interface, (frontend) part of the application

# PostMan Application

API Updates by the videos latest every 10 seconds, can debug using postman, postman collections can be given during review.

http://127.0.0.1:8001/api/get_videos

Status	200 OK

# Steps for Running the Project.

# Clone the Git Repository

git clone 

# Install all the Requirements.

pip install requirements.txt

# Add the Youtube API-Key

Add the Dev Key in settings.

# Video Updating every 25 seconds after 1st March 2020

localhost:8000
http://127.0.0.1:8000/
