from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
# from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea
from django.db.models import Avg, Count
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
# from mptt.fields import TreeForeignKey
# from mptt.models import MPTTModel

from django.dispatch import receiver
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from taggit.managers import TaggableManager



class BlogCategory(MPTTModel):
    parent = TreeForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):       
        return reverse('category_blog', kwargs={'id': self.id, 'slug': self.slug})

    

    def __str__(self):                           # __str__ method elaborated later in
        # post.  use __unicode__ in place of
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/blog/')
    detail = RichTextUploadingField(blank=True)
    video_link = models.CharField(max_length=255, blank=True, null=True)
    top_news = models.BooleanField(default=False)
    top_news_img = models.ImageField(upload_to='images/blog/topnews/', blank=True, null=True)
    tags = TaggableManager(blank=True)
    slug = models.SlugField(null=False, unique=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seo_keywords = models.CharField(max_length=255, blank=True, null=True)
    seo_description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):       
        return reverse('blog_detail', kwargs={'id': self.id, 'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'image'

    def countcomment(self):
        reviews = BlogComment.objects.filter(
            blog=self).aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class BlogComment(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class BlogForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment']


class Gif(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    # image = models.ImageField(blank=True, upload_to='videos/gifs/')

    def __str__(self):
        return self.title


class NewsSlide(models.Model):
    category = models.CharField(blank=True, max_length=50)
    news = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.news
