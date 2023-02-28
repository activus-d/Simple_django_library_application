from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    isbn = models.CharField(max_length=15)

    def __str__(self):
        return self.title