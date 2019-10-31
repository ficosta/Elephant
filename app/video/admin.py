from django.contrib import admin

from .models import Channel, Clip, Favorite

admin.site.register(Channel)
admin.site.register(Clip)
admin.site.register(Favorite)
