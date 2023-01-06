from django.shortcuts import render
from .models import User, UserInfo
from django.http import Http404


# Create your views here.
def sayhello(request):
    return render(request, 'login.html')


def display_users(request):
    users = User.objects.all()
    return render(request, 'login.html', {'users': users})


def userinfo(request, username):
    try:
        myuser = User.objects.get(pk=username)

    except:
        return Http404('Page not found')
    return render(request, 'userinfo.html', {'myuser': myuser})
