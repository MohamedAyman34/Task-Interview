from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User , AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from django.utils import timezone


# Create your models here.
def generator(length = 8):
    code = ''.join(random.choice('1234567890') for _ in range(length))
    return code

USER_TYPE = [
    ('super-admin','super-admin'),
    ('sttuf','stuff'),
    ('customer','customer'),

]

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Profile"),related_name='Profile' ,on_delete=models.CASCADE)
    user_type = models.CharField(_("user_type"), max_length=50 ,choices=USER_TYPE,null=True,blank=True)
    image = models.ImageField(_("Image"), upload_to='profile/',null =True,blank = True)
    code = models.CharField(_("code"), max_length=8 ,default= generator)
    code_used = models.BooleanField(_("Code Used"), default=False)

    def __str__(self) -> str:
        return f"{self.user_type} - {self.user.username}"

# create user --------> create profile
@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

