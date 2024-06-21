from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(models.Manager):
    def username(self, name):
        return super().get_queryset().filter(name=name).exists()
    def email(self, email):
        return super().get_queryset().filter(email=email).exists()
    def get_by_natural_key(self, username):
        return self.get(username=username)
class Users(AbstractUser):
    name = models.CharField(max_length=150, blank=False, null=False)
    user_type = models.CharField(max_length=255, null=False, blank=False)
    specialty = models.CharField(max_length=255, blank=True)
    
   
    class Meta:
        db_table = 'user_authentication'

    user_manager = UserManager()

    def __str__(self):
        return self.name