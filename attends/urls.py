from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.attend, name='attend'),
    path('attend_new/', views.attend_new, name='attend_new')
]
