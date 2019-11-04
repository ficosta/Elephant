from django.db import models
from django.conf import settings

COMPANY_STATUS_CHOICES = (
    (0, 'Desabilitado'),
    (1, 'Habilitado'),
    (2, 'Demonstração'),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    numberLicenses = models.PositiveSmallIntegerField(default=0)
    status = models.PositiveSmallIntegerField(choices=COMPANY_STATUS_CHOICES, default=0)

    def __str__(self):
        return self.name
