from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import MenuItem, Order


# class MenuItemCssForm(ModelForm):
    # class Meta:
        # model = MenuItem
        # fields = ("description")
        # widgets = {
        # "description": TextInput(attrs={"class": "descriptionclass"})
        # }

# class OrderCssForm(ModelForm):
    # class Meta:
        # model = Order
        # fields = ("items", "order_details")
        # widgets = {
        # "items": TextInput(attrs={"class": "itemsclass"}),
        # "order_details" TextInput(attrs={"class": "orderdetailsclass"})
        # }
