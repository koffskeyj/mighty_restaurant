from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm
from django import forms
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

    #order_Completed = forms.ModelChoiceField(queryset=Order.objects.none())
    #table_Paid = forms.ModelChoiceField(queryset=Order.objects.none())
    class Meta:
        model = Order
        fields = ["order_Completed", "table_Paid"]

    # def __init__(self, *args, **kwargs):
        # super(CompleteForm, self).__init__(*args, **kwargs)
        # order_instance = Order()
        # users_order_completed = order_instance('order_Completed')
        # users_table_Paid = order_instance('table_Paid')
        # self.fields['order_Completed'] = ChoiceField(choices=[(users_order_completed, users_order_completed),])
        # self.fields['table_Paid'] = ChoiceField(choices=[(users_table_Paid, users_table_Paid)],)

    def clean(self):
        cleaned_data=super(CompleteForm, self).clean()
        order_Completed = cleaned_data.get('order_Completed')
        table_Completed = cleaned_data.get('table_Paid')
        return cleaned_data


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")

    if created:
        Profile.objects.create(user=instance)
