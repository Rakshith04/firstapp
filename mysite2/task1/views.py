from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'GET':

        return render(request,'adduser.html',locals())

    elif request.method == 'POST':
        print request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)

        if user:
            return redirect('create_users')
        else:
            e = 'invalid credentials'
            return render(request,'adduser.html',locals())


def create_users(request):
    if request.method == 'GET':
        return render(request,'home.html')
    elif request.method == 'POST':
        User.objects.create(username=request.POST.get('username'), password= request.POST.get('password'))
        f = 'user added'
        return render(request, 'home.html', locals())

def user_list(request):
    user1 = User.objects.all()
    return render(request,'user_list.html',locals())