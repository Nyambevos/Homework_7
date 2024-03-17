from sqlalchemy import select, desc, func, and_

from connect_db import session
from models import StudentsGroups, Students, Teachers, Subjects, Grades

TEACHER_NAME= 'Sherry Hensley'
STUDENT_NAME = 'Lisa York'
SUBJECT_NAME = 'Lexicographer',
STUDENTS_GROUP = 1

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    query = (
        select(Students.name,
               func.round(func.avg(Grades.grade), 2)
               .label("average_grade"))
        .join(Students)
        .group_by(Students.name)
        .order_by(desc("average_grade"))
        .limit(5)
    )
    results = session.execute(query).all()
    return results

def select_2(subject_name: str = SUBJECT_NAME):
    # Знайти студента із найвищим середнім балом з певного предмета.
    query = (
        select(Students.name,
               Subjects.subject_name,
               func.round(func.avg(Grades.grade), 2)
               .label("average_grade"))
        .join(Students)
        .join(Subjects)
        .where(Subjects.subject_name == subject_name)
        .group_by(Students.name, Subjects.subject_name)
        .order_by(desc("average_grade"))
        .limit(1)
    )
    results = session.execute(query).all()
    return results

def select_3(subject_name: str = SUBJECT_NAME):
    # Знайти середній бал у групах з певного предмета.

    query = (
        select(Subjects.subject_name,
               StudentsGroups.student_group,
               func.round(func.avg(Grades.grade), 2)
               .label("average_grade"))
        .select_from(Grades)
        .join(Students)
        .join(Subjects)
        .join(StudentsGroups,
              Students.group_id == StudentsGroups.id)
        .where(Subjects.subject_name == subject_name)
        .group_by(Subjects.subject_name,
                  StudentsGroups.student_group)
    )
    results = session.execute(query).all()
    return results

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    query = select(
        func.round(func.avg(Grades.grade), 2)
               .label("average_grade")
    )
    results = session.execute(query).all()
    return results

def select_5(teacher_name: str = TEACHER_NAME):
    # Знайти які курси читає певний викладач.
    query = (
        select(Subjects.subject_name, Teachers.name)
        .join(Teachers)
        .where(Teachers.name == teacher_name)
    )
    results = session.execute(query).all()
    return results

def select_6(student_group: int = STUDENTS_GROUP):
    # Знайти список студентів у певній групі.
    query = (
        select(Students.id, Students.name)
        .join(StudentsGroups)
        .where(StudentsGroups.student_group == student_group)
    )
    results = session.execute(query).all()
    return results

def select_7(subject_name: str = SUBJECT_NAME,
             students_group: int = STUDENTS_GROUP):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    query = (
        select(Students.name,
               Grades.grade,
               StudentsGroups.student_group,
               Subjects.subject_name)
        .join(Subjects)
        .join(Students)
        .join(StudentsGroups)
        .filter(and_(
            Subjects.subject_name == subject_name,
            StudentsGroups.student_group == students_group))
    )
    results = session.execute(query).all()
    return results

def select_8(teacher_name: str = TEACHER_NAME):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    query = (
        select(Teachers.name,
               func.round(func.avg(Grades.grade), 2)
               .label("average_grade"))
        .select_from(Teachers)
        .join(Subjects, Teachers.id == Subjects.teacher_id)
        .join(Grades, Subjects.id == Grades.subject_id)
        .where(Teachers.name == teacher_name)
        .group_by(Teachers.name)
    )
    results = session.execute(query).all()
    return results

def select_9(student_name: str = STUDENT_NAME):
    # Знайти список курсів, які відвідує певний студент.
    query = (
        select(Subjects.subject_name)
        .select_from(Grades)
        .join(Students)
        .join(Subjects)
        .where(Students.name == student_name)
        .group_by(Subjects.subject_name)
    )
    results = session.execute(query).all()
    return results

def select_10(student_name: str = STUDENT_NAME,
              teacher_name: str = TEACHER_NAME):
    # Список курсів, які певному студенту читає певний викладач.
    query = (
        select(Subjects.subject_name)
        .select_from(Grades)
        .join(Students)
        .join(Subjects)
        .join(Teachers)
        .filter(and_(Students.name == student_name,
                     Teachers.name == teacher_name))
        .group_by(Subjects.subject_name)
    )
    results = session.execute(query).all()
    return results

if __name__ == "__main__":
    print(select_10())