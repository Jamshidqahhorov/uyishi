from django.contrib import admin
from django.urls import path,include

from mysite.myapp import views
urlpatterns = [
    path('', views.home, name='homepage')
]
