from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

def Signup(request):
    if request.method == 'POST':
        if request.POST['Permitcode'] == '01067222887':
            if request.POST['password1'] == request.POST['password2']:
                email = request.POST['email']
                password = request.POST['password1']
                user = User.objects.create_user(username = email, password=password)
                auth.login(request, user)
                return redirect('index:index')
            else:
                return render(request, 'Signup.html')
        else:
            return render(request, 'Signup.html')
            
    return render(request, 'Signup.html')


def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username= email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index:index')
        else:
            context = {'error':'No user information !!'}
            return render(request, 'Login.html', context)
    return render(request, 'Login.html')



def Logout(request):
    auth.logout(request)
    return redirect('index:index')




