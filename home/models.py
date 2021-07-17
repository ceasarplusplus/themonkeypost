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



class Setting(models.Model):
    # STATUS = (
    #     ('True', 'True'),
    #     ('False', 'False'),
    # )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = RichTextUploadingField(blank=True)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(null=True, blank=True)
    contact = RichTextUploadingField(null=True, blank=True)
    donate = RichTextUploadingField(null=True, blank=True)
    what_we_do = models.TextField(null=True, blank=True)
    our_mission = models.TextField(null=True, blank=True)
    our_vision = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)
    privacypolicy = RichTextUploadingField(null=True, blank=True)
    tandc = RichTextUploadingField(null=True, blank=True)
    # status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):

   
    email = models.CharField(blank=True, max_length=50)
    phone = models.IntegerField(blank=True) 
    description = models.TextField(blank=True, max_length=255)
    ip = models.CharField(blank=True, max_length=100)
    note = models.CharField(blank=True, max_length=100)
    # date = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['phone', 'email', 'description']
        # widgets = {
        #     'name': TextInput(attrs={'class': 'input col-lg-6 col-md-6 col-sm-6', 'placeholder': 'Name & Surname'}),
        #     'subject': TextInput(attrs={'class': 'input col-lg-6 col-md-6 col-sm-6', 'placeholder': 'Subject'}),
        #     'phone': TextInput(attrs={'class': 'input col-lg-6 col-md-6 col-sm-6', 'placeholder': 'phone'}),
        #     'email': TextInput(attrs={'class': 'input col-lg-6 col-md-6 col-sm-6', 'placeholder': 'Email Address'}),
        #     'message': Textarea(attrs={'class': 'input col-12', 'placeholder': 'Your Message', 'rows': '5'}),
        # }


class Faqs(models.Model):

    question = models.CharField(max_length=200)
    answer = RichTextUploadingField()

    def __str__(self):
        return self.question





class Subscribe(models.Model):
    email = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.email


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {

            'email': TextInput(attrs={'class': 'email-box', 'placeholder': 'Email Address'}),

        }



class Gallery(models.Model):
    CHOICE = (

        ('Tattoo', 'Tattoo'),
        ('Haircut', 'Haircut'),
        ('Event', 'Event'),
        ('Others', 'Others'),
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/')
    choice = models.CharField(max_length=10, choices=CHOICE)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=20, blank=True)
    host = models.CharField(max_length=30, blank=True)
    description = RichTextUploadingField(blank=True)
    detail = RichTextUploadingField(blank=True)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(blank=True, upload_to='app/images/')
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'image'


class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    image = models.ImageField(blank=True, upload_to='app/images/')




class VideoCategory(MPTTModel):
    parent = TreeForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        # post.  use __unicode__ in place of
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Videos(models.Model):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='app/videos/', blank=True)
    podcast = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'image'




class Audios(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='app/videos/', blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title


class Breadcrumb(models.Model):
    news = models.ImageField(blank=True, upload_to='images/breadcrumb/')
    news_detail = models.ImageField(blank=True, upload_to='images/breadcrumb/')
    audio = models.ImageField(blank=True, upload_to='images/breadcrumb/')
    video = models.ImageField(blank=True, upload_to='images/breadcrumb/')
    store = models.ImageField(blank=True, upload_to='images/breadcrumb/')


    def __str__(self):
        return 'Breadcrumb Adverts'


class Nextmatch(models.Model):
    match = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.match