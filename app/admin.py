from django.contrib import admin
from app.models import Profile, Order, MenuItem

admin.site.register(Profile)
admin.site.register([Order, MenuItem])
