from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    Available_TYPE = (
        # Two values for 1st for database char value 2nd for displaying in admin or anywhere
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    book_name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000, null=True, blank=True)
    publication = models.CharField(max_length=200, null=True, blank=True)
    short_des = models.CharField(max_length=500, null=True, blank=True)
    buy_link = models.CharField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    available = models.CharField(max_length=10, choices=Available_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # Many to many with category
    categories = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return f"{self.book_name}   ~{self.author}"


class Category(models.Model):
    name=models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
