import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest20_DRF_Filtering.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
fake = Faker('en_IN')
import random
def emp_data(n=120):
    for i in range(n):
        no = random.randrange(102, 999)
        name = fake.name()
        salary = random.randrange(10000, 90000)
        address = fake.city()
        emps = Employee.objects.get_or_create(no=no, name=name, salary=salary, address=address)


emp_data()
