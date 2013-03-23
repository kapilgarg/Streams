from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'StreamApp.views.home', name='home'),
    url(r'^reader/feeds/(?P<feed_id>\w+)/$', 'StreamApp.views.feeds'),
    url(r'^reader/addfeed/$', 'StreamApp.views.add_new_feed'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
