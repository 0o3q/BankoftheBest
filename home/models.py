from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('data published')
    view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
