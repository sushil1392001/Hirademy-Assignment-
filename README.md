This Django project provides CRUD APIs for managing Assistants including functionalities for creating, reading, updating, and deleting Assistant records.

Installation
Clone the repository:
git clone https://github.com/sushil1392001/Hirademy-Assignment-

Navigate to the project directory:
cd Hirademy-Assignment

Create a virtual environment (optional but recommended):
python -m venv venv

Activate the virtual environment:
On Windows
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Usage
Run the Django development server:
python manage.py runserver

Access the API endpoints:
Create a new Assistan
POST http://localhost:8000/api/assistants/

Retrieve all Assistants
GET http://localhost:8000/api/assistants/

Retrieve, update, or delete a specific Assistant
GET http://localhost:8000/api/assistants/<id>/ PUT http://localhost:8000/api/assistants/<id>/ DELETE http://localhost:8000/api/assistants/<id>/

API Endpoints
POST /api/assistants/: Create a new Assistant. GET /api/assistants/: Retrieve a list of all Assistants. GET /api/assistants//: Retrieve details of a specific Assistant. PUT /api/assistants//: Update details of a specific Assistant. DELETE /api/assistants//: Delete a specific Assistant.

Postman API Testing Documentation
Introduction
This document provides guidelines for testing the APIs for Products, Customers, and Billing endpoints using Postman. The APIs include CRUD operations (Create, Read, Update, Delete) for each resource.

Prerequisites
Postman: Make sure you have Postman installed on your machine. You can download it from postman.com. API Documentation: Have access to the API documentation to understand the request and response formats for each endpoint.

Setting up Postman
1.Open Postman on your machine. 2.Create a new collection for your API tests. 3.Create a new request for each API endpoint within the collection.

Testing Endpoints
GET /api/assistants/ Method: GET Endpoint: http://your-api-url/api/products/

POST /api/assistants/ Method: POST Endpoint: http://your-api-url/api/products/ Body: JSON data representing the new product.

. GET /api/assistants// Method: GET Endpoint: http://your-api-url/api/products/<id>/

PUT /api/assistants// Method: PUT Endpoint: http://your-api-url/api/products/<id>/ Body: JSON data representing the updated product.

DELETE /api/assistants// Method: DELETE Endpoint: http://your-api-url/api/products/<id>/
