from django.conf.urls import patterns, include, url
from django.contrib import admin
from ejemplo.views import *
urlpatterns = patterns('',
    # Examples:

url(r'^sumar/', sumar),
url(r'^fsumar/', fsumar),
url(r'^esclava/', esclava),
url(r'^$', index),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^pepe/', include(admin.site.urls)),
)
