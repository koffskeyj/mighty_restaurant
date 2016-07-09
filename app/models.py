from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

COOK = 'Cook'
SERVER = 'Server'
OWNER = 'Owner'
USER_CHOICES = ((COOK, 'Cook'), (SERVER, 'Server'), (OWNER, 'Owner'))



class Profile(models.Model):
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=30, choices=USER_CHOICES, null=True, blank=True)

class MenuItem(models.Model):
    item_name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.item_name


class Order(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    items = models.ManyToManyField('app.MenuItem', related_name="items")
    details = models.TextField()
    order_Completed = models.BooleanField(default=False)
    table_Paid = models.BooleanField(default=False)


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")

    if created:
        Profile.objects.create(user=instance)
