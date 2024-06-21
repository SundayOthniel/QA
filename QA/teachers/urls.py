from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('dashboard', views.teacher_dashboard, name='teacher_dashboard'),
    path('logout', views.teacher_logout, name='teacher_logout'),
    path('teacher-profile', views.teacher_profile, name='teacher_profile'),
    path('teacher-update-profile', views.teacher_update_profile, name='teacher_update_profile'),
    path('teacher-question/<int:id>', views.teacher_question, name='teacher_question'),
]