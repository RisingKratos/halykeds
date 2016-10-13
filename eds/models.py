from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AbstractUser(models.Model):
    # Connect To Django authorization
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # IS manager?
    is_manager = models.BooleanField(default=False)

    # MAIN USER
    phone = models.CharField(max_length=16, null=True, blank=True, default="")
    profile_image = models.ImageField(upload_to='Images/', blank=True, null=True)
    location = models.CharField(max_length=32, null=True, blank=True, default="")


    #manager
    name = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=64, null=True, blank=True)
    
    # Django authorization
    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            up = AbstractUser(user=user)
            up.save()

    post_save.connect(create_profile, sender=User)
