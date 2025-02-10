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

## Steps to Run the Project

Follow these steps to set up and run the **Company Database Chat Assistant**:

```bash
# 1. Clone the Repository
git clone <repository-url>

# 2. Navigate to the Project Directory
cd company-database-assistant

# 3. Ensure Python 3.x is Installed
python --version
# If not installed, download it from https://www.python.org/downloads/

# 4. Install Dependencies (If Any)
pip install -r requirements.txt
# Skip this step if no requirements.txt exists

# 5. Run the Application
python chat_assistant.py

# 6. Interact with the Assistant by Asking Questions
# Example queries:
# - "Show me all employees in the Sales department"
# - "Who is the manager of the Marketing department?"
# - "List all employees hired after 2022-01-01"

# 7. Exit the Assistant
# Type:
exit
# Or press Ctrl+C
