from django.urls import path, include
from django.urls.resolvers import URLPattern

from .views import BlogView, blog_detail, addblogcomment, category_blog, TagView, highlights, BlogCategoryView


urlpatterns = [
    path('news/', BlogView.as_view(), name='blog'),
    path('highlights/', highlights, name='highlights'),
    path('news/<int:id>/<slug:slug>',
         blog_detail, name='blog_detail'),
    path('news/tags/<slug:slug>',
         TagView.as_view(), name='tag_view'),
    path('addblogcomment/<int:id>', addblogcomment, name='addblogcomment'),
    path('news-category/<int:id>/<slug:slug>',
         BlogCategoryView.as_view(), name='category_blog'),
]