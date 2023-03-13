from django.db import models

# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE, 
        blank=False
    )

    title = models.CharField(max_length=100)
    summary = models.TextField()
    isbn = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.title