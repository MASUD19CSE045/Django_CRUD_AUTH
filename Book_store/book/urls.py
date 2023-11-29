from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('edit_book/<int:id>',views.edit_book , name='edit_book'),
    path('show_book/',views.show_book,name='showbook'),
    path('store_book/',views.store_book,name='storebook'),
    path('delete_book/<int:id>',views.delete_book , name = 'delete_book' )
]