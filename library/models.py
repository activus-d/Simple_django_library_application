from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=50, blank=False, unique=True)
    # Step 1: nullable slug (for existing data)
    # slug = models.SlugField(blank=False, null=True, unique=False, default=None)
    slug = models.SlugField(blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("author", kwargs={"slug": self.slug})
    
class Collection(models.Model):
    name = models.CharField(max_length=50)
    #if you have exisiting data in your database and add a new field to your model, you will get an error while trying to migrate the new fields because django will ask you what to add as the default for the exiting object in your database. Follow these steps to automatically add value for the field you just created.
    # Note: never delete you migration files becaause it can make you lose existing data. Use the command "python manage.py migrate <app name> <migration name or migration number>". Priotize using the migration number instead of name. To migrate to a previous migration before deleting the suceeding migration file.
    # Note: Whenever you change the name a migration, you have to also change the name  migration file in the dependencies =of the suceeding migration file.
    # Step 1: nullable slug (for existing data)
    # slug = models.SlugField(blank=False, null=True, unique=False, default=None)
    # create and empty migration file and add your migration script. Check the 0006_step_2_migrate_slug_data.py for example of this kind of script.
    # for more info you can always run the command "python manage.py migrate --help"
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