from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has info and wants an user now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'users/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'users/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'users/signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user = auth.authenticate(request, username=user_id, password=user_pw)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error' : '아이디나 비밀번호가 틀렸습니다.'})
    else:
        return render(request, 'users/login.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return render(request, 'users/login.html')
    return redirect('home')
