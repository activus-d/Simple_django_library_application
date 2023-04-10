from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)
    # if you have after migrating your models and saving some data in you you intend to create new fields, Django would ask you to provide a defualt value for existing objects in your database. You may also want to automatially use the value of some existing fields as value of you newly added fields. If this is the case, there are steps to take and things to note:
    # First, under no condition should you ever delete you migration files at the first instance to solve such issues. doing that would cause you a lot of problems and make you lose your data. This would be highly detrimental if your project is already in production.
    # then follow the follwoing steps:
    # Step 1: nullable slug (for existing data)
    # slug = models.SlugField(blank=False, null=True, unique=False, default=None)
    # Step 2: migrate back to an old migration file. To do this, enter the following in your command-line terminal "python manage.py migrate <your application name, in this instance "library"> <number or name of old migration file you want to migrate to, in this instance "0004">"
    # if you need further direction, enter the following in your command-line terminal: "python manage.py migrate --help"
    # Step 3: Write a customized migration file just as in migration file 0006_step_2_migrate_slug_data.py of this library application. The file would have a python script which a function that can automatically add value to he existing objects in your database/models.
    slug = models.SlugField(blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("author", kwargs={"slug": self.slug})
    
class Collection(models.Model):
    name = models.CharField(max_length=50)
    # Step 1: nullable slug (for existing data)
    # slug = models.SlugField(blank=False, null=True, unique=False, default=None)
    slug = models.SlugField(blank=False, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("collection", kwargs={"slug": self.slug})
    
class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT, #CASCADE would delete all the book related to an author if the author is deleted but protect will not allow you to delete an author if there are already books related to them
        blank=False,
        related_name='books'
    )

    collection = models.ManyToManyField(Collection, related_name='books')

    title = models.CharField(max_length=100)
    summary = models.TextField()
    isbn = models.CharField(max_length=15, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # Step 1: nullable slug (for existing data)
    # slug = models.SlugField(blank=False, null=True, unique=False, default=None)
    slug = models.SlugField(blank=False, unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book", kwargs={"slug": self.slug})