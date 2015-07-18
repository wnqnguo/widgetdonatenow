from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class FixedS3BotoStorage(S3BotoStorage):
    def url(self, name):
        url = super(FixedS3BotoStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url

class StaticStorage(FixedS3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(FixedS3BotoStorage):
    location = settings.MEDIAFILES_LOCATION