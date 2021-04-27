from django.db import models
from django.urls import reverse


class Post(models.Model):
    title= models.CharField(max_length=500)
    body= models.TextField()
    author= models.CharField(max_length=100, default="")
    img= models.CharField(max_length=2058, default="")
    date= models.DateField(default="")

    def __str__(self):
        return  self.title +'|'+ self.author

    def get_absolute_url(self):
        return reverse('boogie', args=[str(self.id)])