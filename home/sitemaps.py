
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from news.models import Blog, BlogCategory
from store.models import Product, Category


class StaticViewSitemap(Sitemap):
    
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [ 'index', 'blog', 'live_view', 'subscribe', 'videos',
        'odds_view', 'contact', 'tandc','podcast', 'faq', 'donate','privacy_policy',
          'highlights', 'shop',
       'shopcart',
         'login', 'account', 'user_update', 'user_password', 'user_orders',
         'checkout', 'order_completed',
]
        



    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return Blog.objects.all().order_by('id')

    def lastmod(self, obj):
        return obj.updated


class StoreSitemap(Sitemap):

    def items(self):
        return Product.objects.all().order_by('id')
    
    def lastmod(self, obj):
        return obj.update_at

class StoreCategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all().order_by('id')

class BlogCategorySitemap(Sitemap):

    def items(self):
        return BlogCategory.objects.all().order_by('id')