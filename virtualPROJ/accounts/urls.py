from django.urls import path
from .views import UserRegisterView, dashboard
urlpatterns=[
    path('register/', UserRegisterView.as_view(), name='register'),
    path('dashboard',dashboard, name='dashboard' ),


]