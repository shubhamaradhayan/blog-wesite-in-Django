from django.db import models
# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    description=models.TextField(max_length=300)
    image=models.FileField(upload_to="uploads")
    status=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)

class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    msg=models.TextField(max_length=300)
    phone=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)

