from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_ladon import urls as ladon_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api', include(ladon_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
