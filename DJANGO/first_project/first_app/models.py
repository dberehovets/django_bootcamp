from django.db.models import *

# Create your models here.
class Topic(Model):
    top_name = CharField(max_length=264, unique = True)

    def __str__(self):
        return self.top_name


class Webpage(Model):
    topic = ForeignKey(Topic, on_delete=CASCADE)
    name = CharField(max_length=264, unique=True)
    url = URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(Model):
    name = ForeignKey(Webpage, on_delete=CASCADE)
    date = DateField()

    def __str__(self):
        return str(self.date)
