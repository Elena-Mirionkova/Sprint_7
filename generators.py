import datetime
from faker import Faker

fake = Faker('ru_RU')

def generate_login():
    return fake.user_name()
    
def generate_password():
    return fake.password(8)

def generate_name():
    return fake.first_name()

def generate_last_name():
    return fake.last_name()

def generate_address():
    return fake.address()

def generate_metro():
    return fake.random_int(2, 20)

def generate_phone():
    return fake.phone_number()

def generate_time():
    return fake.random_int(1, 10)

def generate_date():
    return str(fake.future_date("+7d"))

def generate_comment():
    return fake.text(20)
