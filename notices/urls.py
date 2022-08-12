from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.notice, name='notice'),
    path('<int:board_id>/', views.notice_detail, name='notice_detail')
]
