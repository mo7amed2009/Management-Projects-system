from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User as main_user
# Create your models here.

class User (AbstractUser):
    ROLE_CHOICES = [
    ('user', 'user'),        # مستخدم عادي
    ('manager', 'manager'),# مدير
    ('junior','junior'),
    ('senior', 'senior'),    # سينيور
]
    

    email=models.EmailField(unique=True)
    position=models.CharField(choices=ROLE_CHOICES,default='user')
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    def __str__(self):
        return self.username
    
    
class Profile(models.Model):

    nickname=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    address=models.TextField(max_length=250,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_profile(sender,created,instance,**kw):
    if created:
        Profile.objects.create(
            user=instance
        )