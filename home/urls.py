from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<int:board_id>/delete', views.delete, name='delete'),
]
