from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Attend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attend = models.CharField(max_length=4)
    created_at = models.DateTimeField('data published')
