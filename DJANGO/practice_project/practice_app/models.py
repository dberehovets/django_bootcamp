from django.db.models import *

# Create your models here.
class User(Model):
    fname = CharField(max_length=264, default='user')
    lname = CharField(max_length=264, default='user')
    email = EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.fname + " " + self.lname
