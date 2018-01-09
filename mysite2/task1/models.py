from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Role(models.Model):
    user = models.OneToOneField(User,related_name='role')
    user_role = models.CharField(max_length=20)



class Role_type(models.Model):
    name = models.CharField(max_length=20)


@receiver(post_save, sender=User)
def create_user_role(sender,instance,created,**kwargs):
    if created and instance.is_superuser:
        user_role = Role.objects.create(user=instance)
        user_role.user_role = 'Admin'
        user_role.save()