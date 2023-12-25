from django.db import models
from django.contrib.auth.models import User
from pets_api.models import Pet

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    users_name = models.CharField(max_length=200, blank=True, null=True) # optional
    date_of_birth = models.DateField(blank=True, null=True) #for registration only
    account_age = models.DateTimeField(auto_now_add=True, blank=True)
    avatar = models.URLField(max_length=300, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    pets = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


