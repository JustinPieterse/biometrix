import sqlite3
from datetime import datetime

class Timesheet:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()
        print("Timesheet database initialized.")

    def create_table(self):
        """
        Creates the timesheet table if it doesn't exist.
        """
        query = """
        CREATE TABLE IF NOT EXISTS timesheet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            event_time TEXT,
            event_type TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def log_event(self, user_id):
        """
        Logs a clock-in or clock-out event.
        """
        event_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO timesheet (user_id, event_time, event_type) VALUES (?, ?, ?)"
        event_type = "clock-in"  # You can add logic to toggle clock-in/clock-out
        self.conn.execute(query, (user_id, event_time, event_type))
        self.conn.commit()
        print(f"Logged {event_type} for User {user_id} at {event_time}")

    def export_to_csv(self, file_path):
        """
        Exports the timesheet data to a CSV file.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM timesheet")
        rows = cursor.fetchall()

        with open(file_path, 'w') as file:
            file.write("ID,User ID,Event Time,Event Type\n")
            for row in rows:
                file.write(','.join(map(str, row)) + '\n')
        print(f"Timesheet exported to {file_path}")
