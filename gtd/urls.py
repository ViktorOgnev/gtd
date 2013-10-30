from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gtd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/?$', 'accounts.views.register', name="register"),
    url(r'', include('core.urls')),
)
