from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('registeration', views.register, name='register'),
]