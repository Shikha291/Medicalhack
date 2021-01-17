from django.urls import path, re_path
from . import views

urlpatterns=[
    path('upload/', views.upload_image, name='upload_image'),
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('attendance_page/', views.attendance_page),
    path('attendance/', views.attendance, name='attendance'),
    re_path('final/', views.final, name="final"),

]