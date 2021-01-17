from django.urls import path
from . import views

urlpatterns=[
    path('upload', views.upload_image, name='upload_image'),
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('attendance/', views.attendance, name='attendance')

]