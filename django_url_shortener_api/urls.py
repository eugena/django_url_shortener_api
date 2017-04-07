"""django_url_shortener_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from shortener.views import GoToLinkView

urlpatterns = [
    url(r'^(?P<code>\w{%s})' % settings.CODE_LENGTH, GoToLinkView.as_view()),
    url(r'^', include('api.urls')),
]
