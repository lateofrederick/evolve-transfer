from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split(' ')
    if css_classes and arg not in css_classes:
        css_classes = '{} {}'.format(' '.join(css_classes), arg)
    else:
        css_classes = ' '.join(css_classes)
    return value.as_widget(attrs={'class': css_classes})
