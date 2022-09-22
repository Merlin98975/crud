
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    
    path('create/',views.create),
    path('read/',views.read),
    path('single/<int:pk>/', views.read_one),
    path('update/<int:pk>/',views.update),
    path('delete/<int:pk>/',views.delete)
]