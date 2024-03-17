import logging
import faker
from datetime import datetime
from random import randint

from src.connect_db import session
from src.models import StudentsGroups, Students, Teachers, Subjects, Grades

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20

def generate_fake_data(
        number_students,
        number_teachers,
        number_subjects) -> tuple:
    fake_students = []  # тут зберігатимемо студентів
    fake_teachers = []  # тут зберігатимемо викладачів
    fake_subjects = []  # тут зберігатимемо предмети

    fake_data = faker.Faker()

    # Створимо набір студентів у кількості number_students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Згенеруємо тепер number_teachers кількість викладачів'''
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # Та number_subjects набір предметів
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    return fake_students, fake_teachers, fake_subjects

# students, teachers, subjects
def insert_data_to_db(students, teachers, subjects) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними
    for_groups = []
    for group in range(1, NUMBER_GROUPS + 1):
        for_groups.append(StudentsGroups(student_group = group))
    session.add_all(for_groups)
    session.commit()

    for_students = []
    for student in students:
        for_students.append(Students(name = student, group_id = randint(1, NUMBER_GROUPS)))
    session.add_all(for_students)
    session.commit()

    for_teachers = []
    for teacher in teachers:
        for_teachers.append(Teachers(name = teacher))
    session.add_all(for_teachers)
    session.commit()

    for_subjects = []
    for subject in subjects:
        for_subjects.append(Subjects(subject_name = subject, teacher_id = randint(1, NUMBER_TEACHERS)))
    session.add_all(for_subjects)
    session.commit()

    for_grades = []
    for id in range(1, NUMBER_STUDENTS + 1):
        for _ in range(randint(1, NUMBER_GRADES)):
            grade_date = datetime(2023, randint(9, 12), randint(1, 30))
            for_grades.append(Grades
                (student_id = id,
                 subject_id = randint(1, NUMBER_SUBJECTS),
                 date_of = grade_date,
                 grade = randint(1, 5)))
    session.add_all(for_grades)
    session.commit()

    logging.info(f'Fake data is written to the database')


if __name__ == "__main__":
#    groups, students, teachers, subjects, evaluations = prepare_data(
#        *generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS))
#
#    insert_data_to_db(groups, students, teachers, subjects, evaluations)
    students, teachers, subjects = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS)
    insert_data_to_db(students, teachers, subjects)
