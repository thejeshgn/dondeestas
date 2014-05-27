from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin,auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import misc.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^api/', include('api.urls')),

    #admin related urls
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^$', misc.views.Home.as_view(),
        name='home',),

)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
