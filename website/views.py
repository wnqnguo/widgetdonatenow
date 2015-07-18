# coding: utf-8
from django.template import RequestContext
from django.template import Context
from django.shortcuts import render_to_response, redirect
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.conf import settings
from core.models import *
from core.forms import *
from django.core.urlresolvers import resolve


class HomePageView(TemplateView):
    template_name = "%s/home.html" % settings.SITE_NAME


class TermsView(TemplateView):
    template_name = "%s/terms.html" % settings.SITE_NAME


class PrivacyView(TemplateView):
    template_name = "%s/privacy.html" % settings.SITE_NAME


class FaqView(TemplateView):
    template_name = "%s/faq.html" % settings.SITE_NAME


class AboutView(TemplateView):
    template_name = "%s/about.html" % settings.SITE_NAME


class HowItWorksView(TemplateView):
    template_name = "%s/how_it_works.html" % settings.SITE_NAME


class WidgetsView(TemplateView):
    template_name = "%s/widgets.html" % settings.SITE_NAME

    def get_context_data(self, **kwargs):
        context = super(WidgetsView, self).get_context_data(**kwargs)
        context.update({'current_url': 'widgets'})
        return context


class PaymentsView(TemplateView):
    template_name = "%s/payments.html" % settings.SITE_NAME
    
    def get_context_data(self, **kwargs):
        context = super(PaymentsView, self).get_context_data(**kwargs)
        context.update({'current_url': 'payments'})
        return context


class WithdrawsView(TemplateView):
    template_name = "%s/withdraws.html" % settings.SITE_NAME
    
    def get_context_data(self, **kwargs):
        context = super(WithdrawsView, self).get_context_data(**kwargs)
        context.update({'current_url': 'withdraws'})
        return context

class LandingpageView(TemplateView):
    template_name = "%s/landingpage.html" % settings.SITE_NAME

class DiscoverView(TemplateView):
    template_name = "%s/discover.html" % settings.SITE_NAME

def account(request, *args, **kwargs):
    context = RequestContext(request)

    context.push({'current_url': resolve(request.path_info).url_name})

    return render_to_response("%s/account.html" % settings.SITE_NAME, context)


def contact(request, *args, **kwargs):
    context = RequestContext(request)

    form = None

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            form = None
            messages.success(request, _(u'Sucess!.'))
        else:
            messages.error(request, _(u'Error. Check the form fields.'))

    if not form:
        form = ContactForm()

    context.push({'form': form})

    return render_to_response("%s/contact.html" % settings.SITE_NAME, context)

def login(request, *args, **kwargs):
    context = RequestContext(request)

    return render_to_response("%s/contact.html" % settings.SITE_NAME, context)

def signup(request, *args, **kwargs):
    context = RequestContext(request)

    return render_to_response("%s/contact.html" % settings.SITE_NAME, context)

def recovery(request, *args, **kwargs):
    context = RequestContext(request)

    return render_to_response("%s/contact.html" % settings.SITE_NAME, context)

def reset(request, *args, **kwargs):
    context = RequestContext(request)

    return render_to_response("%s/contact.html" % settings.SITE_NAME, context)
