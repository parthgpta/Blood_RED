from django.shortcuts import render, get_object_or_404 , redirect
from .models import Person
from .forms import SignUpForm
from .forms import donateForm
from django.contrib.auth import login,authenticate

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.blood_group = form.cleaned_data.get('blood_group')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.about_me = form.cleaned_data.get('about_me')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def donate_blood(request):
    form = donateForm(request.POST)
    if request.method =="POST":
        
        if form.is_valid():
            person = form.save(commit =False)
            person.name = request.user
            person.address= form.cleaned_data.get('address')
            person.blood_grp = form.cleaned_data.get('blood_grp')
            person.phone = form.cleaned_data.get('phone')
            person.email = form.cleaned_data.get('email')
            person.save()            
            return redirect('main_page')
   
    
    return render(request , 'Profile/donate_blood_req.html',{'form':form})


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

def person_profile(request):
    return render(request , 'registration/profile.html' ,{})
