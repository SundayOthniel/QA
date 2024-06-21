from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import StudentQuestion
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teachers.models import QuestionAnswer

@login_required(login_url='base:login')
def student_dashboard(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        specialty = request.POST.get('speciality')
        
        if user.name != name and user.email != email:
            messages.error(request, 'This is not your email or name')
            return redirect('student:student_dashboard')
        else:
            messages.success(request, 'Question sucessfully asked')
            student_question = StudentQuestion.question_manager.create(student=user,name=name, email=email, question=question, specialty=specialty)
            student_question.save()
            return redirect('student:student_question_page')
    return render(request, 'studentdashboard.html')

@login_required(login_url='base:login')
def student_profile(request):
    user = request.user
    return render(request, 'studentprofile.html',{'user':user})

@login_required(login_url='base:login')
def student_question_page(request):
    user = request.user
    questions = StudentQuestion.question_manager.filter(student=user)
    return render(request, "studentquestionpage.html", {'questions':questions})

@login_required(login_url='base:login')
def student_answer(request, id):
    question_answer = StudentQuestion.question_manager.get(id=id) 
    # question = QuestionAnswer.objects.get(id=id) 
    return render(request, 'studentanswer.html', {'question_answer':question_answer})

@login_required(login_url='base:login')
def student_update_profile(request):
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            name = request.POST.get("name")
            email = request.POST.get("email")
            uname = request.POST.get("uname")
            userr = request.POST.get("user")
            user.name = name
            user.email = email
            user.username = uname
            user.user = userr
            user.save()
            return redirect('teacher:teacher_profile' )
    return render(request, 'teachereditprofile.html')

@login_required(login_url='base:login')
def student_logout(request):
    logout(request)
    if 'student' in request.session:
        del request.session['student']
    return redirect('base:login') 

def delete_question(request, id):
    question = get_object_or_404(StudentQuestion, id=id)
    return render(request, 'question_delete.html', {'question': question})

def delete_question_confirm(request, id):
    question = get_object_or_404(StudentQuestion, id=id)
    question.delete()
    return redirect('student:student_question_page')