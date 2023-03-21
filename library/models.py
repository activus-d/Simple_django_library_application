from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
class Collection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT, #CASCADE would delete all the book related to an author if the author is deleted but protect will not allow you to delete an author if there are already books related to them
        blank=False
    )

    collection = models.ManyToManyField(Collection)

    title = models.CharField(max_length=100)
    summary = models.TextField()
    isbn = models.CharField(max_length=15, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title