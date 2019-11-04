from django.db import models
from django.contrib.auth.models import User

LOG_EVENT_CHOICES = (
    (0, 'Informação'),
    (1, 'Erro'),
    (2, 'Aviso'),
)

NOTIFICATION_STYLE_CHOICES = (
    (0, 'Critical'),
    (1, 'Query'),
    (2, 'Warning'),
    (3, 'Information'),
)

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    event = models.PositiveSmallIntegerField(choices=LOG_EVENT_CHOICES, default=0)
    eventDescription = models.CharField(max_length=250)
    createdAt = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    description = models.CharField(max_length=250)
    style = models.PositiveSmallIntegerField(choices=NOTIFICATION_STYLE_CHOICES, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
