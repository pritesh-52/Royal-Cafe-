"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('insert/',views.insert,name="insert"),
    path('conform/<int:pk>',views.conformpage,name="conform"),
    path('accepted/<int:pk>',views.accepted,name="accepted"),  #pass the pk
    path('rejected/<int:pk>',views.rejected,name="rejected"),
    path('signin/',views.signinpage,name="signin"),
    path('usersignin/',views.admin,name="usersignin"),
    path('show/',views.showpage,name="show"),
    path('admin/', views.signinpage,name="admin"),
]
