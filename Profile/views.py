from django.shortcuts import render, get_object_or_404
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class signupview(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



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

def person_detail(request ,pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request , 'Profile/person_detail.html' , {'person':person})
