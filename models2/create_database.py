from faker import Faker
from models2.database import create_db, Session
from models2.employee import Employee


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    faker = Faker('ru_RU')
    department_list = ['Бухгалтерия', 'Отдел продаж', 'Юридический отдел', 'Цех', 'Склад', 'Транспортный отдел']
    session.commit()

    for i in range(30):
        if i % 2 == 0:
            name = faker.name_female()
        else:
            name = faker.name_male()
        age = faker.random.randint(21, 60)
        phone_number = faker.phone_number()
        address = faker.street_address()
        email = faker.ascii_free_email()
        department = faker.random.choice(department_list)
        experience = faker.random.randint(1, 5)
        salary = faker.random.randint(20000, 50000)
        employees = Employee(name, age, phone_number, address, email, department, experience, salary)
        session.add(employees)

    session.commit()
    session.close()
