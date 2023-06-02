from django import template

register = template.Library()


@register.filter
def get_item(list, index):
    return list[index] if len(list) > index else None
