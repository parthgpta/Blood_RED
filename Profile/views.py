from django.shortcuts import render
from .models import Person

# Create your views here.

def main_page(request):
    return render(request , 'Profile/main_page.html',{})

def dis_pageA(request):
    persons = Person.objects.filter(blood_grp='A')
    return render(request , 'Profile/dis_page.html',{'persons':persons})

def dis_pageB(request):
    persons = Person.objects.filter(blood_grp='B')
    return render(request , 'Profile/dis_page.html',{'persons':persons})

def dis_pageO(request):
    persons = Person.objects.filter(blood_grp='O')
    return render(request , 'Profile/dis_page.html',{'persons':persons})
