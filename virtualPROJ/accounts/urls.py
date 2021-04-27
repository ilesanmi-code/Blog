from django.urls import path
from .views import UserRegisterView, dashboard
urlpatterns=[
    path('register/', UserRegisterView.as_view()),
    path('dashboard',dashboard, name='dashboard' ),


]