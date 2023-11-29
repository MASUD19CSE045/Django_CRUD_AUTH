from django import forms 
from todoapp.models import TodoItemModel

class TodoItemForm(forms.ModelForm): 
    class Meta:
        model=TodoItemModel
        fields=['title','description','priority','due_date','completed']