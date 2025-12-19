from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null = True, blank =True)
    profile_photo = models.ImageField(upload_to= 'profile_photos/', null = True, blank = True)
    
    def __str__(self):
        return f"{self.profile_photo}"
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth = None, profile_photo = None):
        user = self.model(username = username, email = email, date_of_birth = date_of_birth, profile_photo = profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, date_of_birth = None, profile_photo = None):
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        return self.create_user(username, email, password=password)
        

        




    






