from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(max_length=2000)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
    ADMIN = 'admin', _('admin')

class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=UserRoles.choices)
    age = models.PositiveSmallIntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        def __str__(self):
            return self.name