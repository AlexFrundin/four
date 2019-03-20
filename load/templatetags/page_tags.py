from django import template

register = template.Library()

@register.filter(name='get_before_page')
def get_before(value, arg):

    arg = int(arg)
    left_lim = arg-5
    if left_lim<1:left_lim=1
    return range(left_lim, arg)


@register.filter(name='get_after_page')
def get_after(value,arg):
    arg=int(arg)
    right_lim=arg+5
    if right_lim>len(value):right_lim=len(value)
    return range(arg+1, right_lim+1)
