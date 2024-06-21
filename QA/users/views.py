from django.contrib.auth import authenticate, login
from .models import Users
from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    uname = request.POST.get("uname")
    user_type = request.POST.get("user_type")
    speciality = request.POST.get("speciality")
    password = request.POST.get("pass")
    c_pass = request.POST.get("c_pass")
    
    name_exist = Users.user_manager.username(name)
    emil_exist = Users.user_manager.username(email)
    if request.method == "POST":
        if name_exist:
            messages.error(request, f"This user \"{name}\" already exist")
            return redirect('base:register')
        elif password != c_pass:
            messages.error(request, f"Password does not match")
            return redirect('base:register')
        elif emil_exist:
            messages.error(request, f"This provided \"{email}\" already exist")
            return redirect('base:register')
        elif password == c_pass:
            if user_type == 'student':
                user_type = Users.user_manager.create(username=uname.lower(), name=name, email=email, user_type=user_type)
                user_type.set_password(password)
                user_type.save()
                return redirect('base:login')
            else:
                try:
                    user_type = Users.user_manager.create(username=uname, name=name, email=email, user_type=user_type, specialty=speciality)
                    user_type.set_password(password)
                    user_type.save()
                    return redirect('base:login')
                except:
                    messages.error(request, "Check all fields")
    return render(request, 'loginandregistration/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('uname').lower()
        password = request.POST.get('password')
        authenticate_user = authenticate(username=username, password=password)
        if authenticate_user is not None:
            if authenticate_user.user_type == 'teacher':
                request.session['teacher'] = 'teacher'
                login(request, authenticate_user) 
                return redirect('teacher:teacher_dashboard')
            else:
                request.session['student'] = 'student'
                login(request, authenticate_user) 
                return redirect('student:student_dashboard')
        else:
            messages.error(request, "Reconfirm your login details")
            return redirect('base:login')
    return render(request, 'loginandregistration/login.html')