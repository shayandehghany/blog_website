# blog/templatetags/nav_active.py
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    try:
        if context["request"].resolver_match.url_name == url_name:
            return "active"
    except Exception:
        return ""
    return ""
