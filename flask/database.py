import psycopg2
from os import environ
from datetime import datetime, timezone

class Tasks:
    def __init__(self) -> None:
        hostname = environ["DATABASE_HOST"]
        username = environ["POSTGRES_USER"]
        password = environ["POSTGRES_PASSWORD"]
        database = environ["POSTGRES_DB"]
        
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
    
    def __del__(self) -> None:
        self.cur.close()
        self.connection.close()

    def getTasks(self) -> list[dict]:
        self.cur.execute("SELECT * FROM tasks ORDER BY created_at DESC")
        
        data = [{"task_id": element[0],
                 "created_at": element[1],
                 "task_time": element[2],
                 "description": element[3],
                 "completed": element[4]} for element in self.cur.fetchall()]

        return data

    def addTask(self, description: str, task_time: str) -> None:
        current_time = datetime.now(timezone.utc)
        self.cur.execute("""
            INSERT INTO tasks (created_at, task_time, description, completed) 
            VALUES (%(created_at)s, %(task_time)s, %(description)s, %(completed)s)
        """, {
            "created_at": current_time,
            "task_time": task_time if task_time else None,
            "description": description,
            "completed": False
        })
        
        self.connection.commit()

    def updateTaskStatus(self, task_id: int, completed: bool) -> None:
        self.cur.execute("UPDATE tasks SET completed = %s WHERE task_id = %s", (completed, task_id))
        self.connection.commit()

    def deleteTask(self, task_id: int) -> None:
        self.cur.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
        self.connection.commit()
