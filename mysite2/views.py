from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_passwords
from django.core.mail import send_mail



def create_users(request):
    if request.method == 'GET':
        return render(request, 'home.html')

    elif request.method == 'POST':
        password1 = request.POST.get('password')
        user_email = request.POST.get('email')
        username = request.POST.get('username')
        User.objects.create(username=username, password=make_password(request.POST.get('password')), email=user_email)
        f = 'user added'
        send_mail(
            'user credentials',
            'username-' + username+',' + 'password-' + password1,
            '',
            [user_email],
            fail_silently=False,
        )
        return render(request, 'home.html', locals())

def user_login(request):
    if request.method == 'GET':
        return render(request, 'adduser.html', locals())

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return redirect('create_users')
        else:
            e = 'invalid credentials'
            return render(request, 'adduser.html', locals())


def user_lists(request):
    user1 = User.objects.all()
    return render(request, 'user_list.html', locals())

