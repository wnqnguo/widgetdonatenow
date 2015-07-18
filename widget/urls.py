"""widget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from website.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^terms/?', TermsView.as_view(), name='terms'),
    url(r'^privacy/?', PrivacyView.as_view(), name='privacy'),
    url(r'^faq/?', FaqView.as_view(), name='faq'),
    url(r'^about/?', AboutView.as_view(), name='about'),
    url(r'^how-it-works/?', HowItWorksView.as_view(), name='how-it-works'),
    url(r'^contact/?', contact, name='contact'),

    url(r'^logout/?', login, name='logout'),
    url(r'^login/?', login, name='login'),
    url(r'^signup/?', signup, name='signup'),
    url(r'^recovery/?', recovery, name='recovery'),
    url(r'^reset/?', reset, name='reset'),

    url(r'^widgets/?', WidgetsView.as_view(), name='widgets'),
    url(r'^payments/?', PaymentsView.as_view(), name='payments'),
    url(r'^withdraws/?', WithdrawsView.as_view(), name='withdraws'),
    url(r'^account/?', account, name='account'),
    url(r'^landingpage/?', LandingpageView.as_view(), name='landingpage'),
    url(r'^discover/?', DiscoverView.as_view(), name='discover'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
