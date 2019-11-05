from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

COMPANY_STATUS_CHOICES = (
    (0, 'Desabilitado'),
    (1, 'Habilitado'),
    (2, 'Demonstração'),
)

PROFILE_ROLES_CHOICES = (
    (0, 'Nivel 1'),
    (1, 'Nivel 2'),
    (2, 'Nivel 3'),
)


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    numberLicenses = models.PositiveSmallIntegerField(default=0)
    status = models.PositiveSmallIntegerField(choices=COMPANY_STATUS_CHOICES, default=0)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    emailNotify = models.BooleanField(default=True)
    roles = models.PositiveSmallIntegerField(choices=PROFILE_ROLES_CHOICES, default=0)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
