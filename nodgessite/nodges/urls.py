from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('nodgessite.nodges.views',
    (r'^nodes/(?P<node_id>\d+)/$', 'detail'), 
    (r'^nodes/(?P<node_id>\d+)/update$', 'update'),
)
