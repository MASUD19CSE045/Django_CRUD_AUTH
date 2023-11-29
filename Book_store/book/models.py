from django.db import models

# Create your models here.
class BookStoreModel(models.Model):

    CATEGORY=(
        ('mistry','mistry'),
        ('chai-fi','chai-fi'),
        ('mistry','mistry'),
        ('mistry','mistry'),
    )
    id=models.IntegerField(primary_key=True)
    book_name=models.CharField( max_length=50)
    author=models.CharField(max_length=40)
    category=models.CharField( max_length=50,choices=CATEGORY)
    first_pub=models.DateTimeField(auto_now_add=True)
    last_pub=models.DateTimeField(auto_now=True)