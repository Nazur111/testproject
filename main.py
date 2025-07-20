import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id ITEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
major TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
course_id ITEGER PRIMARY KEY AUTOINCREMENT,
course_name TEXT

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_courses(
id ITEGER PRIMARY KEY AUTOINCREMENT,
course_id INTENGER,
student_id INTENGER
FOREIGN KEY(course_id) REFERENCES courses(id),
FOREIGN KEY(student_id) REFERENCES students(id)
)
""")