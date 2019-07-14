from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('',views.main_page , name = 'main_page'),
    path('group/A/' ,views.dis_pageA , name = 'dis_pageA'),
    path('group/B/' ,views.dis_pageB , name = 'dis_pageB'),
    path('group/O/' ,views.dis_pageO , name = 'dis_pageO'),
    path('login/',auth_views.login , name ='login'),
    path('logout/' , auth_views.logout , {'next_page':'/'} ,name = 'logout'),
    path('signup/' , views.signup , name='signup'),
    path('person/<int:pk>/', views.person_detail ,name='person_detail'),
    path('person/profile/' ,views.person_profile , name='person_profile'),
    path('person/donate_blood_req/' , views.donate_blood , name='donate_blood_req'),
    
    ]
