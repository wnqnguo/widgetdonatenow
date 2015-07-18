# coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

from django.contrib.sites.models import Site
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import post_save

import string
import random

from django.conf import settings

class AccountManager(BaseUserManager):

    def create_user(self, username, name, email, site, password=None):
        site_ref = Site.objects.get(pk=site)
        user = self.model(name=name, username=username, email=self.normalize_email(email), site=site_ref)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, email, site, password):
        user = self.create_user(username, name=name, email=email, site=site, password=password)
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


# django.contrib.auth.get_user_model()
class Account(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    site = models.ForeignKey(Site)

    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    document = models.CharField(max_length=30, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    confirmation_key = models.CharField(max_length=50, null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    slug = models.SlugField(max_length=20, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    cover = models.ImageField(upload_to='profile/covers/', default='profile/covers/no-cover.jpg')
    about = models.TextField(null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=1)

    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'site']

    def save(self, *args, **kwargs):
        if not self.id:
            self.confirmation_key = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(settings.CONFIRMATION_CODE_SIZE) )

            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(settings.SLUG_SIZE) )
            self.access_code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(settings.ACCESS_CODE_SIZE) )

        self.username = "%s|%s" % (self.email, self.site.id)

        return super(Account, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    # django definition methods for AbstractBaseUser
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Contact(models.Model):
    email = models.EmailField(max_length=255)
    message = models.TextField()

    account = models.ForeignKey(Account, null=True, blank=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    status = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
