from django import template
from django.core.cache import cache

register = template.Library()


@register.inclusion_tag("core/object_list.html")
def object_list(objects, color):
    """
    Usage {% object_list some_context_variable %}
    """
    return {"object_list": objects,
            "color": color}




