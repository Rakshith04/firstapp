from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from . models import *


#@login_required()
def create_users(request):
    if request.method == 'GET':
        return render(request,'home.html')

    elif request.method == 'POST':

        password1 = request.POST.get('password')
        user_email = request.POST.get('email')
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        s= User.objects.create(username=username, password=password,email=user_email)


       # user_role = User.objects.get(id=s.id)
       # user_role.name = Role.POST.get('role')
       # user_role.save()

        #role = Role_type.objects.all()
        #return render(request, 'home.html',locals())

        f = 'user added'


    send_mail(
            'user credentials',
            'user created successfully'+'\nHere is the password-'+ password1 +  'and username-' + username +'',
            'rakshithbm87@gmail.com',
            [user_email],
            fail_silently=False,
        )
    return render(request, 'home.html', locals())

def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html',locals())

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            return HttpResponseRedirect('https://www.amazon.in/')
        else:
            e = 'invalid credentials'
            return render(request,'login.html',locals())


def user_list(request):
    user1 = User.objects.all()
    return render(request,'user_list.html',locals())


