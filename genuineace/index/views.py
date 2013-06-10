# Create your views here.

from django.shortcuts import render_to_response as RTR
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from Company.models import Account
import hashlib
def home(request):
    """ url method for index page """
    if request.user.is_authenticated:
        print 'y'
    else:
        print 'm'
    cdic = {
        'is_authenticated' : request.user.is_authenticated,
        'user' : request.user,
        }
    return RTR('index.html', cdic)

def logout_view(request):
    """ log out """
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    """ register page """
    if request.method == 'GET':
        return RTR('register.html', '', context_instance = RequestContext(request))
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = Account(email = email, 
            password = hashlib.md5(password).hexdigest(), 
            is_active = 'N',
            first_name = 'kymo')
        user.save()
        if user:
            return HttpResponse('yes')
        else:
            return HttpResponse('no')

def login_view(request):
    """ login page """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print email, password
        user = authenticate(email = email, password = password)
        if user:
            #save the user information
            login(request, user)
            return HttpResponseRedirect('/') 
        else:
            return HttpResponse('login failed')
    return RTR('login.html', '', context_instance = RequestContext(request))
