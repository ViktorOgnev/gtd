from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^/?$', 'core.views.blank_redirect',
        # name='core_blank_redirect'),
        
    url(r'^(?P<status>[-\w]*)/?$', 'core.views.item_list_and_form',
        name='core_item_list_and_form'),
    
        
    url(r'^item/(?P<slug>[-\w]+)/?$', 'core.views.item_detail',
        name='core_item_detail'),
        
    # url(r'^project-plan/(?P<slug>[-\w]+)/?$', 'core.views.project_plan',
        # name='core_project_plan'),
        
    # url(r'^calendar/(?P<slug>[-\w]+)/?$', 'core.views.calendar',
        # name='core_calendar'),
        
    # url(r'^waiting/?$', 'core.views.waiting',
        # name='core_waiting'),
        
    # url(r'^next-actions/?$', 'core.views.next-actions',
        # name='core_next_actions'),
        
    # url(r'^trash/?$', 'core.views.trash',
        # name='core_trash'),
        
    # url(r'^someday-maybe/?$', 'core.views.someday_maybe',
        # name='core_someday_maybe'),
        
    # url(r'^references/?$', 'core.views.references',
        # name='core_references'),
        
    # url(r'^reference/(?P<slug>[-\w]+)?$', 'core.views.next-actions',
        # name='core_next_actions'),
    
        
)