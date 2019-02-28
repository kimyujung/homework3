from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm, LoginForm
from django.contrib.auth import login, authenticate


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'error' : '이미 존재하는 사용자명입니다'})
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form' : form})
            

def signin(request):
    if request.method == 'POST' :
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error' : 'Username과 비밀번호가 일치하지 않습니다'})
    else:
        form = LoginForm()
        return render(request, 'signin.html', {'form' : form})

def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')