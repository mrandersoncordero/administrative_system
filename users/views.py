"""Users views."""

# Django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def sign_in(request):
    if (request.method == 'GET'):
        return render(request, 'users/login.html')
    else:
        username = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request, username=username, password=passwd)

        if user:
            login(request, user)
            return HttpResponse('User login succes')
        else:
            return render(request, 'users/login.html', {
                'error': 'Invalid Username or password'
            })



