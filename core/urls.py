from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^/?$', 'core.views.blank_redirect',
        # name='core_blank_redirect'),
    url(r'^/?$', 'core.views.all_actions',
        name='core_all_actions'),    
    
    url(r'load-item-form/?$', 'core.views.ajax_load_edit_item_form',
        name='core_load_edit_item_form'),
        
    url(r'^remove-item/?$', 'core.views.ajax_remove_item',
        name='core_remove_item'),
    
    url(r'^item-list/(?P<status>[-\w]*)/?$', 'core.views.item_list_and_form',
        name='core_item_list_and_form'),
    
    url(r'^item/(?P<slug>[-\w]+)/?$', 'core.views.item_detail',
        name='core_item_detail'),
    
    
        
 
        
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