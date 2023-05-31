from django.db import models

# Create your models here.
class positiondb(models.Model):
    position=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="Profile")

class playerdb(models.Model):
    playerposition=models.CharField(max_length=100,null=True,blank=True)
    playername=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    club=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="productimage")