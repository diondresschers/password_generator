from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'36878763(*&@^)'}) # the last part is the Dictionary that is sent to the Template-file index.html

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQSTUVWXUZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    thepassword = ''
    for x in range (0, length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    name = '(wo)man'

    return render(request, 'generator/about.html', {'name':name})


