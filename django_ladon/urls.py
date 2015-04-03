from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django_ladon.views import ladon_view

urlpatterns = patterns('',
                       url(r'^(/.*)$', csrf_exempt(ladon_view)),
                       )
