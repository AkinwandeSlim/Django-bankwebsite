
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from PIL import Image

from django.contrib.auth import get_user_model




class CustomUser(AbstractUser):
    # pass
    account_id = models.CharField(max_length=10, unique=True, primary_key=True,default='2000000000')
    username = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.username





class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,)
    phone = models.CharField(max_length=15, blank=True)
    image = models.ImageField(default='team-4.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    account_balance = models.FloatField(default=0.0)
    




    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height <400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)




@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()