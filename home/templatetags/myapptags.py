from django import template
from django.urls import reverse

from home.models import VideoCategory, Setting, Breadcrumb, Advert
from news.models import BlogCategory,  Blog
from store.models import ShopCart

register = template.Library()


@register.simple_tag
def blogcategories():
    return BlogCategory.objects.all()


@register.simple_tag
def videocategories():
    return VideoCategory.objects.all()



@register.simple_tag
def shopcartcount(userid):
    count = ShopCart.objects.filter(user_id=userid).count()
    return count

@register.simple_tag
def settingstag():
    setting = Setting.objects.get(pk=1)
    return setting


@register.simple_tag
def shopcarttag(userid):
    shopcart = ShopCart.objects.filter(user_id=userid)
    return shopcart

@register.simple_tag
def totaltag(userid):
    total = 0
    shopcart = ShopCart.objects.filter(user_id=userid)
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    return total
    

@register.simple_tag
def newstrendfooter():
    return Blog.objects.filter(top_news=True).order_by('-id')[:3]

@register.simple_tag
def newstrendheader():
    return Blog.objects.filter(top_news=True).order_by('-id')[:3]


@register.simple_tag
def advertisements():
    return Advert.objects.all()


@register.simple_tag
def breadcrumbs():
    return Breadcrumb.objects.get(pk=1)


@register.simple_tag
def poptags():
    return Blog.tags.most_common()[:15]


