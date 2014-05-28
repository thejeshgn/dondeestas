from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin,auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from misc import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(),),
    url(r'path/', views.DisplayPath.as_view(),name='path',),
)

urlpatterns +=  patterns('',
    # Examples:
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
