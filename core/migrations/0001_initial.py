# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=255)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('document', models.CharField(max_length=30, null=True, blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('confirmation_key', models.CharField(max_length=50, null=True, blank=True)),
                ('verified_at', models.DateTimeField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('cover', models.ImageField(default=b'profile/covers/no-cover.jpg', upload_to=b'profile/covers/')),
                ('about', models.TextField(null=True, blank=True)),
                ('purpose', models.TextField(null=True, blank=True)),
                ('status', models.IntegerField(default=1)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('status', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
