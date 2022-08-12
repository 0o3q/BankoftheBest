from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField('data published')
    hit = models.IntegerField()

    def __str__(self):
        return self.title