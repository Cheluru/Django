from django.urls import path
from app1 import views
from django.conf import *
urlpatterns=[
    path('',views.feed,name="home"),
    path('login',views.loginView,name="login"),
    path('register',views.register,name='register'),
    path('post',views.postView,name='post'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logoutView,name='logout'),
    path('one/<int:rid>',views.onepost,name='op'),
    path('delete/<int:rid>',views.dele,name='dele'),
]