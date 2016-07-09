from django.contrib import admin
from django.forms import SelectMultiple
from app.models import Profile, Order, MenuItem
from django.db import models

admin.site.register(Profile)
admin.site.register([Order, MenuItem])
