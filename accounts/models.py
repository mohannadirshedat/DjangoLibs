from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Company(models.Model):
    Name = models.CharField(max_length=250 , verbose_name="Company Name ")

    def __str__(self):
        return self.Name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Email  = models.EmailField(max_length=500, blank=True , verbose_name="Email")
    company= models.ForeignKey(Company,on_delete=models.CASCADE , blank=True , null=True)
    Phone = models.CharField(max_length=30, blank=True, verbose_name="Phone ")
    SSN  = models.CharField(max_length=30, blank=True, verbose_name="SSN")
    Address  = models.CharField(max_length=30, blank=True, verbose_name="Address ")
    photo = models.FileField()


    def __str__(self):
        return self.Email
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()