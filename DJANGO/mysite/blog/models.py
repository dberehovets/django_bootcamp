from django.db.models import *
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(Model):
    author = ForeignKey('auth.User', on_delete=CASCADE)
    title = CharField(max_length=200)
    text = TextField()
    create_date = DateTimeField(default=timezone.now())
    published_date = DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(Model):
    post = ForeignKey('blog.Post', related_name='comments', on_delete=CASCADE)
    author = CharField(max_length=200)
    text = TextField()
    create_date = DateTimeField(default=timezone.now())
    approved_comment = BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
