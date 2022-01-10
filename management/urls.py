# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib.auth import views as auth_views
from management import views

urlpatterns = [

     # URLS Frontend
    path('login', views.login_view, name='login'),
    path('', views.home.as_view(), name='home'), 
    path('logout',  views.logout_view, name='logout'),
    path('detail_vehicle/<int:pk>/', views.detail_vehicle, name='detail_vehicle'),

]
