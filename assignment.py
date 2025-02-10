import sqlite3
import re

class ChatAssistant:
    def __init__(self, db_name="company.db"):
        self.db_name = db_name
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create Employees table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Department TEXT NOT NULL,
                Salary INTEGER NOT NULL,
                Hire_Date TEXT NOT NULL
            )
        ''')

        # Create Departments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Departments (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL UNIQUE,
                Manager TEXT NOT NULL
            )
        ''')

        # Insert initial data if not already present
        cursor.execute("SELECT COUNT(*) FROM Employees")
        if cursor.fetchone()[0] == 0:
            cursor.executemany('''
                INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?, ?)
            ''', [
                (1, "Alice", "Sales", 50000, "2021-01-15"),
                (2, "Bob", "Engineering", 70000, "2020-06-10"),
                (3, "Charlie", "Marketing", 60000, "2022-03-20")
            ])

        cursor.execute("SELECT COUNT(*) FROM Departments")
        if cursor.fetchone()[0] == 0:
            cursor.executemany('''
                INSERT INTO Departments (ID, Name, Manager) VALUES (?, ?, ?)
            ''', [
                (1, "Sales", "Alice"),
                (2, "Engineering", "Bob"),
                (3, "Marketing", "Charlie")
            ])

        conn.commit()
        conn.close()

    def execute_query(self, query, params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            conn.close()
            return result
        except sqlite3.Error as e:
            conn.close()
            return f"Database error: {str(e)}"

    def handle_query(self, user_input):
        user_input = user_input.strip().lower()

        # Handle different types of queries
        if match := re.match(r"show me all employees in the (.+?) department", user_input):
            department = match.group(1).strip()
            query = "SELECT Name FROM Employees WHERE Department = ?"
            result = self.execute_query(query, (department,))
            return [row[0] for row in result] if result else f"No employees found in the {department} department."

        elif match := re.match(r"who is the manager of the (.+?) department\?", user_input):
            department = match.group(1).strip()
            query = "SELECT Manager FROM Departments WHERE Name = ?"
            result = self.execute_query(query, (department,))
            return result[0][0] if result else f"No manager found for the {department} department."

        elif match := re.match(r"list all employees hired after (\d{4}-\d{2}-\d{2})", user_input):
            date = match.group(1).strip()
            query = "SELECT Name FROM Employees WHERE Hire_Date > ?"
            result = self.execute_query(query, (date,))
            return [row[0] for row in result] if result else f"No employees were hired after {date}."

        elif match := re.match(r"what is the total salary expense for the (.+?) department\?", user_input):
            department = match.group(1).strip()
            query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
            result = self.execute_query(query, (department,))
            return f"Total salary expense for {department}: {result[0][0] if result[0][0] else 0}" if result else f"No salary data for {department}."

        else:
            return "Sorry, I didn't understand that question. Please try again."

    def run(self):
        print("Welcome to the Company Database Assistant!")
        print("Type 'exit' to quit the assistant.")
        while True:
            try:
                user_input = input("Ask a question: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Goodbye!")
                    break
                response = self.handle_query(user_input)
                print(response)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    assistant = ChatAssistant()
    assistant.run()
