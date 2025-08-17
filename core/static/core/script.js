// // Add Employee
// document.getElementById('employee-form').addEventListener('submit', function(e) {
//     e.preventDefault();
//     fetch('/api/add-employee/', {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify({
//             name: document.getElementById('name').value,
//             email: document.getElementById('email').value,
//             department: document.getElementById('department').value,
//             joining_date: document.getElementById('joining_date').value
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('employee-response').textContent = data.message || JSON.stringify(data);
//     });
// });

// // Apply Leave
// document.getElementById('leave-form').addEventListener('submit', function(e) {
//     e.preventDefault();
//     fetch('/api/apply-leave/', {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify({
//             email: document.getElementById('leave-email').value,
//             start_date: document.getElementById('start_date').value,
//             end_date: document.getElementById('end_date').value,
//             reason: document.getElementById('reason').value
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('leave-response').textContent = data.message || JSON.stringify(data);
//     });
// });


// fetch('/api/employees/')
//   .then(response => response.json())
//   .then(data => {
//     console.log(data); // Show all employees in browser console
//   });



//   function showEmployees() {
//   fetch('/api/employees/')
//     .then(response => response.json())
//     .then(data => {
//       const list = document.getElementById('employees');
//       list.innerHTML = '';
//       data.forEach(emp => {
//         const li = document.createElement('li');
//         li.textContent = emp.name + ' | ' + emp.email + ' | ' + emp.department + ' | Joined: ' + emp.joining_date;
//         list.appendChild(li);
//       });
//     });
// }

// // Call on page load
// showEmployees();

// // Optionally, call showEmployees() after adding a new employee to keep the list updated



// Add Employee
document.getElementById('employee-form').addEventListener('submit', function(e) {
    e.preventDefault();
    fetch('/api/add-employee/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            department: document.getElementById('department').value,
            joining_date: document.getElementById('joining_date').value
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('employee-response').textContent = data.message || JSON.stringify(data);
        showEmployees(); // Update the employee list after adding an employee
    });
});

// Apply Leave
document.getElementById('leave-form').addEventListener('submit', function(e) {
    e.preventDefault();
    fetch('/api/apply-leave/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            email: document.getElementById('leave-email').value,
            start_date: document.getElementById('start_date').value,
            end_date: document.getElementById('end_date').value,
            reason: document.getElementById('reason').value
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('leave-response').textContent = data.message || JSON.stringify(data);
    });
});

// Show employees in the UI
function showEmployees() {
    fetch('/api/employees/')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('employees');
            list.innerHTML = '';
            data.forEach(emp => {
                const li = document.createElement('li');
                li.textContent = emp.name + ' | ' + emp.email + ' | ' + emp.department + ' | Joined: ' + emp.joining_date;
                list.appendChild(li);
            });
        });
}

// Call on page load
showEmployees();

