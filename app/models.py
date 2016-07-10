from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm
COOK = 'Cook'
SERVER = 'Server'
OWNER = 'Owner'
USER_CHOICES = ((COOK, 'Cook'), (SERVER, 'Server'), (OWNER, 'Owner'))

YES = 'YES'
NO = 'NO'
COMPLETED_CHOICES = ((YES, 'YES'), (NO, 'NO'))


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
    order_Completed = models.CharField(max_length=30, choices=COMPLETED_CHOICES, default='NO')
    table_Paid = models.CharField(max_length=30, choices=COMPLETED_CHOICES, default='NO')


class CompleteForm(ModelForm):
    class Meta:
        model = Order
        fields = ["order_Completed", "table_Paid"]


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")

    if created:
        Profile.objects.create(user=instance)
