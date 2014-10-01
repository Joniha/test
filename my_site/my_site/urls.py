from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('my_site.myapp.views',
	url(r'^$', 'run', name='run'),
	url(r'^modifies/$', 'get', name='my'),
    url(r'^modifies/up$', 'update', name='update'),
    url(r'^modifies/in/', 'insert', name='insert'),
    url(r'^admin/', include(admin.site.urls)),
)
