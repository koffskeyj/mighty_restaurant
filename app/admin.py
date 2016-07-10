from django.contrib import admin
from django.forms import SelectMultiple, Textarea
from app.models import Profile, Order, MenuItem
from django.db import models

class OrderAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size': 100})},
                            models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols': 10})}, }


admin.site.register(Profile)
admin.site.register(Order, OrderAdmin)
admin.site.register(MenuItem)
