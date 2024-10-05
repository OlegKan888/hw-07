import random
from datetime import datetime
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import (
    Base,
    Group,
    Student,
    Teacher,
    Subject,
    Grade,
)  # заміни models на свій файл з моделями

# Підключення до бази даних
engine = create_engine(
    "sqlite:///database.db"
)  # Заміни на свій зв'язок, якщо використовуєш PostgreSQL
Session = sessionmaker(bind=engine)
session = Session()

# Створення об'єкту Faker
fake = Faker()

# Створення груп
groups = [Group(name=f"Group {i+1}") for i in range(3)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(fullname=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

# Створення предметів
subjects = [
    Subject(name=fake.word().capitalize(), teacher=random.choice(teachers))
    for _ in range(5)
]
session.add_all(subjects)
session.commit()

# Створення студентів
students = [
    Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(30)
]
session.add_all(students)
session.commit()

# Створення оцінок
grades = []
for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 20)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.uniform(1, 10),
                date_received=fake.date_between(start_date="-1y", end_date="today"),
            )
            grades.append(grade)

session.add_all(grades)
session.commit()

print("Database seeding complete.")
