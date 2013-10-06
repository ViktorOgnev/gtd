from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    url(r'^in-basket/?', 'core.views.inbasket',
        name='core_inbasket'),
    url(r'^projects/$, 'core.views.projects',
        name='core_projects'),
    url(r'^project-plan/(?P<slug>[-\w]+)/?$', 'core.views.project_plan',
        name='core_project_plan'),
    url(r'^calendar/(?P<slug>[-\w]+)/?$', 'core.views.calendar',
        name='core_calendar'),
    url(r'^waiting/?$', 'core.views.waiting',
        name='core_waiting'),
    url(r'^next-actions/?$', 'core.views.next-actions',
        name='core_next_actions'),
    url(r'^trash/?$', 'core.views.trash',
        name='core_trash'),
    url(r'^someday-maybe/?$', 'core.views.someday_maybe',
        name='core_someday_maybe'),
    url(r'^references/?$', 'core.views.references',
        name='core_references'),
    url(r'^reference/(?P<slug>[-\w]+)?$', 'core.views.next-actions',
        name='core_next_actions'),
)