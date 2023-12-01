from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    thumbnail = models.ImageField(blank = True)

    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."

