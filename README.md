README.md
# Company Database Chat Assistant

This is a simple and interactive **SQLite-based Chat Assistant** for managing and querying a company database. It supports handling queries related to employee information, departments, and salary expenses.

---

## Features

- Store and manage information for **employees** and **departments**.
- Query employee details based on department and hire date.
- Retrieve department manager information.
- Calculate total salary expenses for a department.
- Pre-populated initial data for demo purposes.

---

## Database Schema

### Employees Table
| Column     | Type    | Description              |
|------------|---------|--------------------------|
| ID         | INTEGER | Primary key               |
| Name       | TEXT    | Employee's name           |
| Department | TEXT    | Department name           |
| Salary     | INTEGER | Employee salary           |
| Hire_Date  | TEXT    | Date of hiring (YYYY-MM-DD)|

### Departments Table
| Column     | Type    | Description              |
|------------|---------|--------------------------|
| ID         | INTEGER | Primary key               |
| Name       | TEXT    | Department name (Unique)  |
| Manager    | TEXT    | Department manager        |

---

## Query Examples

You can ask the assistant the following types of questions:

1. **Show employees in a department:**  
2. **Get department manager:**  
3. **List employees hired after a specific date:**  
4. **Get total salary expense for a department:**  

---

## Installation

1. Clone the repository:
```bash
git clone <repository-url>

---


## Navigate to project directory
cd company-database-assistant


---

##Run the project
python assignment.py

---
