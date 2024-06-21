from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('dashboard', views.student_dashboard, name='student_dashboard'),
    path('student-profile', views.student_profile, name='student_profile'),
    path('student-logout', views.student_logout, name='student_logout'),
    path('student-question-page', views.student_question_page, name='student_question_page'),
    path('student-update-profile', views.student_update_profile, name='student_update_profile'),
    path('student-answer/<int:id>', views.student_answer, name='student_answer'),
    path('delete-question/<int:id>', views.delete_question, name='delete_question'),
    path('delete-question-confirm/<int:id>', views.delete_question_confirm, name='delete_question_confirm'),
]