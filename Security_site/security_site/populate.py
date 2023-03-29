import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'security_site.settings')
import django
django.setup()

from accounts.models import Employee
from faker import Faker

fake = Faker(locale='en_US')

def crate_employee(number:int):

    for _ in range(number):

        employee = Employee(first_name=fake.first_name(), 
                    last_name=fake.last_name(), 
                    email=fake.email(), 
                    phone_number=fake.msisdn())
        print(employee)

        employee.save()
    print(f"CREATED {number} Customers")
        
crate_employee(50)