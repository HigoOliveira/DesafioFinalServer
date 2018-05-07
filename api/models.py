from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
  name = models.CharField(max_length=255)
  phone = PhoneNumberField(unique=True)

  objects = UserManager()

  USERNAME_FIELD = 'phone'
  REQUIRED_FIELDS = []

  def __str__(self):
    return "%s - %s" % (self.phone.as_national, self.name)

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')

class Event(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  where = models.CharField(max_length=255)
  datetime = models.DateTimeField()