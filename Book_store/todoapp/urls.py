from django.urls import path
from .import views
urlpatterns = [
    path('addtodo/',views.addtodo ,name='addtodo'),
    path('show_todo/',views.showtodo,name='showtodo',),
    path('update_todo/<int:id>',views.updatetodo,name='update_todo'),
    path('delete_todo/<int:id>',views.delete_todo,name='delete_todo'),
]
