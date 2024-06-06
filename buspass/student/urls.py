from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stu/', views.stu, name='stu'),
    path('apply/', views.apply, name='apply'),
    path('chkst/', views.chkst, name='chkst')
]
