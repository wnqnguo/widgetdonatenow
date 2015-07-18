# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import check_password
from core.models import Account

class CustomAuthBackend(object):

    def authenticate(self, username=None, password=None):

        try:
            site = Site.objects.get(pk=settings.SITE_ID)
            username = "%s|%s" % (username, site.id)
            user = Account.objects.get(username=username)
            pwd_valid = check_password(password, user.password)

            if pwd_valid:
                return user

        except Account.DoesNotExist:
            pass
        
        return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
