from django.urls import path
from  .views import Home, BlogView, BlogPost

urlpatterns = [
    path('',  Home.as_view(), name='blog'),
    path('article/<int:pk>', BlogView.as_view(), name='article-details'),
    path('post_blog', BlogPost.as_view(), name='post'),

]