from django.contrib import admin

from .models import Log, Notification

admin.site.register(Log)
admin.site.register(Notification)