from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from model import Student, Grade, Course, Teacher, Group  # Приклад імпорту моделей
from database import engine

Session = sessionmaker(bind=engine)


def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    session = Session()
    result = (
        session.query(Student, func.avg(Grade.value).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .limit(5)
        .all()
    )
    session.close()
    return result


def select_2(subject_id):
    # Знайти студента із найвищим середнім балом з певного предмета
    session = Session()
    result = (
        session.query(Student, func.avg(Grade.value).label("avg_grade"))
        .join(Grade)
        .filter(Grade.course_id == subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .first()
    )
    session.close()
    return result


def select_3(subject_id):
    # Знайти середній бал у групах з певного предмета
    session = Session()
    result = (
        session.query(Group.name, func.avg(Grade.value).label("avg_grade"))
        .join(Student)
        .join(Grade)
        .filter(Grade.course_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    session.close()
    return result


def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    session = Session()
    result = session.query(func.avg(Grade.value)).scalar()
    session.close()
    return result


def select_5(teacher_id):
    # Знайти які курси читає певний викладач
    session = Session()
    result = session.query(Course).filter(Course.teacher_id == teacher_id).all()
    session.close()
    return result


def select_6(group_id):
    # Знайти список студентів у певній групі
    session = Session()
    result = session.query(Student).filter(Student.group_id == group_id).all()
    session.close()
    return result


def select_7(group_id, subject_id):
    # Знайти оцінки студентів у окремій групі з певного предмета
    session = Session()
    result = (
        session.query(Student.name, Grade.value)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.course_id == subject_id)
        .all()
    )
    session.close()
    return result


def select_8(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    session = Session()
    result = (
        session.query(func.avg(Grade.value).label("avg_grade"))
        .join(Course)
        .filter(Course.teacher_id == teacher_id)
        .scalar()
    )
    session.close()
    return result


def select_9(student_id):
    # Знайти список курсів, які відвідує певний студент
    session = Session()
    result = (
        session.query(Course)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )
    session.close()
    return result


def select_10(student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач
    session = Session()
    result = (
        session.query(Course)
        .join(Grade)
        .filter(Grade.student_id == student_id, Course.teacher_id == teacher_id)
        .distinct()
        .all()
    )
    session.close()
    return result
