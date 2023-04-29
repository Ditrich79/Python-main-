from sqlalchemy import Column, Integer, String
from models2.database import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer)
    phone_number = Column(Integer)
    address = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    department = Column(String(250), nullable=False)
    experience = Column(Integer)
    salary = Column(Integer)

    def __init__(self, name, age, phone_number, address, email, department, experience, salary):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.department = department
        self.experience = experience
        self.salary = salary

    def __repr__(self):
        return f"Сотрудник: (ФИО: {self.name}, Возраст: {self.age}, Номер телефона: {self.phone_number}, " \
               f"Адрес проживания: {self.address}, Электронная почта: {self.email}, Стаж работы: {self.experience}, " \
               f"Зарплата: {self.salary})"
