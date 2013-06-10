from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from index.views import home, login_view, register_view, logout_view
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'genuineace.views.home', name='home'),
    # url(r'^genuineace/', include('genuineace.foo.urls')),
    url(r'^$', home),
    url(r'^login/', login_view),
    url(r'^register/', register_view),
    url(r'^logout/', logout_view),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
