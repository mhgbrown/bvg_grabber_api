from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import api.home
import api.actual
import api.scheduled

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bvg_grabber_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', api.home.index, name='index'),
    url(r'^actual', api.actual.show, name='show'),
    url(r'^scheduled', api.scheduled.show, name='show'),
    url(r'^admin', include(admin.site.urls)),
)
