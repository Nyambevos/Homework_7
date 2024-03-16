from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

# Таблиця груп
class StudentsGroups(Base):
    __tablename__ = "students_group"
    id = Column(Integer, primary_key=True)
    student_group = Column(Integer, nullable=False, unique=True)

# Таблиця студентів
class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey('students_group.id'))

# Таблиця викладачів
class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

# Таблиця предметів
class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(255), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

# Таблиця оцінок
class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    date_of = Column(DateTime)
    grade = Column(Integer, nullable=False)

