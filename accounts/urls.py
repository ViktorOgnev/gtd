from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'accounts.views.register', name='register'),
        
)    