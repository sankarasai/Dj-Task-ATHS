from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('signup',views.signup),
    path('home',views.home),
    path('update/<int:id>/',views.update),
    path('adminpage',views.admin),
    path('adminupdate/<int:id>/',views.adminupdate)
]