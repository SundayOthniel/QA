from django.shortcuts import render, get_object_or_404
from students.models import StudentQuestion
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import QuestionAnswer

@login_required(login_url='base:login')
def teacher_dashboard(request):
    user = request.user
    if user.specialty is not None:
        question_count = StudentQuestion.question_manager.specialised_questions_count(specialty=user.specialty)
        questions = StudentQuestion.question_manager.get_specialised_questions(specialty=user.specialty)
    context = {'questions':questions, 'question_count':question_count}
    return render(request, 'teacherdashboard.html', context)

@login_required(login_url='base:login')
def teacher_profile(request):
    return render(request, 'teacherprofile.html')

@login_required(login_url='base:login')
def teacher_update_profile(request):
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            name = request.POST.get("name")
            email = request.POST.get("email")
            uname = request.POST.get("uname")
            user_type = request.POST.get("user_type")
            user.name = name
            user.email = email
            user.username = uname
            user.user_type = user_type
            user.save()
            return redirect('teacher:teacher_profile' )
    return render(request, 'teachereditprofile.html')

@login_required(login_url='base:login')
def teacher_logout(request):
    logout(request)
    if 'teacher' in request.session:
        del request.session['teacher']
    return redirect('base:login') 

@login_required(login_url='base:login')
def teacher_question(request, id):
    question = get_object_or_404(StudentQuestion, id=id)
    if request.method == 'POST':
        teacher_answer = request.POST.get('answer')
        answer = QuestionAnswer.objects.create(answer=teacher_answer)
        answer.save()
    return render(request, 'teacheranswer.html', {'question':question})