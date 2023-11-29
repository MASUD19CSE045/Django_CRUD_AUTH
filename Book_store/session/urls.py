from django.urls import path
from .import views
urlpatterns = [
    path('login',views.login_form ,name='login'),
    path('logouta',views.logout_form ,name='logouta'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_form, name='signup'),
    path('changepass/', views.change_password, name='changepass'),
]