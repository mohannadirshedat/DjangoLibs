from django.db import models
from django.contrib.auth.models import User ,Group

from django.urls import reverse


class Company(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class Profile(models.Model):
    User_Name = models.OneToOneField(User,on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to="profiles/media/")
    Email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255,blank=True,null=True)
    Phone = models.CharField(max_length=255, null=True,blank=True)
    SSN = models.CharField(max_length=255,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profiles', kwargs={'pk': self.pk})



    def __str__(self):
        return self.Email

class ProfileAdmin(models.Model):
    users = models.OneToOneField(User,on_delete=models.CASCADE)
    User_Roll = models.ForeignKey(Group,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)







