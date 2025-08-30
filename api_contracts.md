## 📌 API Contracts

### 1. Add Employee
**POST /employees**

Request:
```json
{
  "name": "Sakshi",
  "email": "sakshi@example.com",
  "department": "HR",
  "joining_date": "2025-01-10"
}
Response:

{
  "message": "Employee added successfully",
  "employee_id": 1

}

##  Apply for Leave
POST /leaves

Request
{
  "employee_id": 1,
  "start_date": "2025-09-01",
  "end_date": "2025-09-05",
  "leave_type": "Casual"
}
Response:
{
  "message": "Leave request submitted",
  "leave_id": 101
}


3. Approve/Reject Leave

PUT /leaves/{leave_id}

Request
{
  "status": "Approved",
  "remarks": "Enjoy your leave"
}
Response:

{
  "message": "Leave updated successfully"
}

