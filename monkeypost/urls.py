from django.contrib import admin
import debug_toolbar
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from django.contrib.sites.models import Site
from home.sitemaps import StaticViewSitemap, BlogSitemap, StoreSitemap, StoreCategorySitemap, BlogCategorySitemap


sitemaps = {
    'static': StaticViewSitemap, 
    # 'blog': BlogSitemap,
    'store': StoreSitemap,
    'storecategory': StoreCategorySitemap,
    'blogcategory': BlogCategorySitemap
}

news_sitemap = {
    'news': BlogSitemap,
    # 'blogcategory': BlogCategorySitemap
}

handler400 = 'home.views.handler400'
handler403 = 'home.views.handler403'
handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'

urlpatterns = [
    path('monkey-admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('news.urls')),
    path('', include('store.urls')),
    path('', include('users.urls')),
    path('', include('order.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    # path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
    #      name='django.contrib.sitemaps.views.sitemap'),


    path('news_sitemap.xml', views.index, {'sitemaps': news_sitemap}),
    path('news_sitemap-<section>.xml', views.sitemap, {'sitemaps': news_sitemap, 'template_name': 'sitemap/my_sitemap.html'},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),



    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)


admin.site.index_title = "The Monkey Post"
admin.site.site_header = "The Monkey Post Admin"
admin.site.site_header = "The Monkey Post Admin"




if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
