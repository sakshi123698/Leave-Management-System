# Leave Management System

## Overview
A Django-based mini leave management system for a startup (MVP).

## Features
- Add employees (Name, Email, Department, Joining Date)
- Apply for leave
- Approve/Reject leave requests
- Track leave balance per employee
- Small Edge case validations

## Setup Steps
1. Clone the repo:https://github.com/sakshi123698/Leave-Management-System


2. Install dependencies:
pip install -r requirements.txt

3. Run migrations:
python manage.py migrate

4. Start server:
python manage.py runserver


5. Access UI: [http://127.0.0.1:8000/lms/]
6. Optional: [http://127.0.0.1:8000/admin/]  (For Accessing Admin Side)







The system is hosted on PythonAnywhere:

Hosted at: https://sakshi123698.pythonanywhere.com




## Assumptions
- All employees start with 20 days leave balance, editable in admin.

## Edge Cases Handled
- Applying before joining date
- Leave on weekends only
- Overlapping leave requests
- Invalid dates
- Leave balance limits
- Duplicate employee email, and more




## API Endpoints (sample)
- Add employee: `/api/add-employee/`
- Apply leave: `/api/apply-leave/`
- Update leave status: `/api/update-leave-status/`
- Leave balance: `/api/leave-balance/`
- List employees: `/api/employees/`



High Level System Design
System Architecture Overview
My Leave Management System uses a client-server architecture, designed for simplicity and scalability:

Frontend Client:
This could be a browser UI for HR/admins, API clients like Postman, or any application that consumes the REST endpoints. The client sends HTTP requests to the backend for all operations (adding employees, applying for leave, etc.).

Backend (Django REST API):
The backend is built with Django and Django REST Framework. It receives requests from the client, processes business logic (validations, leave calculations, overlap checks, etc.), and interfaces with the database using Django's ORM.

Database:
The data layer consists of a relational database (SQLite used in development; PostgreSQL/MySQL recommended for production). All employee, leave, and status data is persisted here. The backend performs CRUD operations via Django ORM.


When the client sends a request (for example, to apply for leave), the backend validates the request, performs checks (for leave balance, valid dates, overlapping requests), and then updates or fetches data from the database.

Responses (success or error) are sent back to the client.

Data consistency and integrity are maintained through Django models and ORM logic.

Class Diagram / Data Model
The core entities are modeled as:

Employee:
Fields: name, email (unique), department, joining_date, leave_balance
Each employee can have multiple leave requests.

LeaveRequest:
Fields: employee (foreign key), start_date, end_date, reason, status (Pending/Approved/Rejected)
Status tracks the approval flow. Relationship is one (employee) to many (leave requests).

![Class Diagram](UML-Diagram_-Employee-Leaveability Approach

If the company grows from 50 to 500+ employees:

Backend:
The Django API can be scaled horizontally—multiple workers or containerized deployments behind a load balancer.

Database:
For larger datasets, migrate to PostgreSQL/MySQL. Use proper indexing (e.g., email, date fields) for efficient queries. Optimize ORM queries and use pagination for employee/leave lists.

Extensibility:
Modular code structure allows for the addition of more features (custom leave types, department hierarchies, multi-level approval).

Performance:
Caching for repeated queries, asynchronous processing for notifications/report generation, integration with task queues if needed.

Diagrams Provided
Architecture Diagram:
Shows main system components and data flow.
See: Architectural-Digram.drawio.jpg

Class Diagram:
Visual representation of models and their relationship.
See: UML-Diagram_-Employee-LeaveRequest.jpg

Assumptions and Design Choices
All employees start with 20 days of leave (editable).

Leave requests must be for future dates and not just weekends.

Only HR/admin processes approvals.

Users are uniquely identified by email.

Strict edge case handling for overlapping requests, invalid dates, and duplicate emails.

Potential Improvements
Add support for different leave types (sick, casual, etc.).

Department-wise leave approvers.

Email/SMS notifications for leave status.

Analytics/reporting features for HR.

Integrate with frontend frameworks for a richer web UI.

## Author
Sakshi Gupta
(Sakshii55421@gmail.com)






