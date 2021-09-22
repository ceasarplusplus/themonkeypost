from django.urls import path, include
from django.urls.resolvers import URLPattern
from django.views.decorators.cache import cache_page

from .views import BlogView, blog_detail, addblogcomment, highlight_json, category_blog, TagView, highlights, BlogCategoryView


urlpatterns = [
    path('news/', BlogView.as_view(), name='blog'),
    path('highlight-json/', highlight_json, name='highlight-json'),
    path('match-highlights/', highlights, name='highlights'),
    path('news/<slug:slug>',
         blog_detail, name='blog_detail'),
    path('news/tags/<slug:slug>',
         cache_page(60 * 10)(TagView.as_view()), name='tag_view'),
    path('addblogcomment/<int:id>', addblogcomment, name='addblogcomment'),
    path('news-category/<int:id>/<slug:slug>',
         BlogCategoryView.as_view(), name='category_blog'),
]