from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sites.models import Site
from home.sitemaps import StaticViewSitemap, BlogSitemap, StoreSitemap, StoreCategorySitemap, BlogCategorySitemap


sitemaps = {
    'static': StaticViewSitemap, 
    'blog': BlogSitemap,
    'store': StoreSitemap,
    'storecategory': StoreCategorySitemap,
    'blogcategory': BlogCategorySitemap
}


handler400 = 'home.views.handler400'
handler403 = 'home.views.handler403'
handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('news.urls')),
    path('', include('store.urls')),
    path('', include('users.urls')),
    path('', include('order.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
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
