from django.db import models

# Create your models here.
class TodoItemModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(
        max_length=20,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        default='medium'
    )
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
  
  
