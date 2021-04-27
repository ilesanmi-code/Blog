from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title= models.CharField(max_length=500)
    body= models.TextField()
    author= models.CharField(max_length=100, default="")
    date= models.DateField(default="")

    def __str__(self):
        return  self.title +'|'+ self.author

    def get_absolute_url(self):
        return reverse('article-details', args=[str(self.id)])
class Comment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-comment_date"]

    def __str__(self):
        return "{}".format(self.description)