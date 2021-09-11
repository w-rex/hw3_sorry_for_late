from django.db import models

# Create your models here.


class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    major = models.CharField(max_length=100)
    direction = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)


class Blog(models.Model):
    image = models.ImageField(upload_to='blog_pics/')
    tittle = models.CharField(max_length=150)
    description = models.TextField()
    hashtags = models.TextField()