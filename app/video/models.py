from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

CHANNEL_STATUS_CHOICES = (
    (0, 'Desabilitado'),
    (1, 'Habilitado'),
)

CLIP_STATUS_CHOICES = (
    (0, 'Indisponivel'),
    (1, 'Disponivel'),
)

class Channel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    hiresLifetime = models.PositiveSmallIntegerField(default=0)
    lowresLifetime = models.PositiveSmallIntegerField(default=0)
    logo = models.ImageField(upload_to='logo/', blank=True)
    status = models.PositiveSmallIntegerField(choices=CHANNEL_STATUS_CHOICES, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Channel, self).save(*args, **kwargs)


class Clip(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='clips')
    recordDate = models.DateTimeField(null=True)
    length = models.PositiveSmallIntegerField(default=0)
    posterURL = models.ImageField(blank=True, upload_to='poster/')
    thumbsURL = models.ImageField(blank=True, upload_to='thumbs/')
    lowresURL = models.URLField(blank=True)
    hiresURL = models.URLField(blank=True)
    status = models.PositiveSmallIntegerField(choices=CLIP_STATUS_CHOICES, default=0)

    # hora do upload
    def __str__(self):
        return str(self.id) + str(self.channel.name) + str(self.recordDate)


class Favorite(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    frame = models.PositiveSmallIntegerField(default=0)
    description = models.CharField(max_length=250)
