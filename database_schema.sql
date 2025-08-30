-- Employee Table
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50),
    joining_date DATE NOT NULL,
    leave_balance INT DEFAULT 20
);

-- LeaveRequest Table
CREATE TABLE LeaveRequest (
    leave_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    leave_type VARCHAR(20) CHECK (leave_type IN ('Sick', 'Casual', 'Earned')),
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);
