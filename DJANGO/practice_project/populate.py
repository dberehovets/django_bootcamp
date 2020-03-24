import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice_project.settings')

import django
django.setup()

from practice_app.models import User
from faker import Faker

fakegen = Faker()

for i in range(20):
    User.objects.get_or_create(fname=fakegen.first_name(), lname=fakegen.last_name, email=fakegen.email())[0]
