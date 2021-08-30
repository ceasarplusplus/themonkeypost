from django.shortcuts import render
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as u_login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from taggit.models import Tag


from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
# from .tokens import account_activation_token
import random
import json
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
import requests
from django.core import serializers
from .models import Audios, Nextmatch, Videos, VideoCategory, ContactMessage, ContactForm, Setting, Subscribe, SubscribeForm, Faqs, Breadcrumb, Nextmatch
from news.models import Blog, BlogCategory, NewsSlide
# Create your views here.

class IndexView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'
    ordering = ['-date']

    paginate_by = 15

    # def get_queryset(self):
    #     return Blog.objects.filter(tags__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = Videos.objects.all()
        top_trends = Blog.objects.filter(top_news=True)
        next_match = Nextmatch.objects.get(pk=1)
        news_slide = NewsSlide.objects.all()[:6]
        context.update({'videos': videos,
                        'news_slide': news_slide,
                        'top_trends': top_trends,
                        'next_match': next_match,
       
                        
                        })
        return context



class AudiosView(ListView):
    model = Audios
    template_name = 'audios.html'
    context_object_name = 'audios'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        news_slide = NewsSlide.objects.all()[:6]
        context.update({
                        'news_slide': news_slide,
                        
       
                        
                        })
        return context

  
class VideosView(ListView):
    model = Videos
    template_name = 'videostest.html'
    context_object_name = 'videos'
    ordering = ['-id']

    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_category = VideoCategory.objects.all()
        podcast = Videos.objects.filter(podcast=True)
        news_slide = NewsSlide.objects.all()[:6]
        context.update({'video_category': video_category,
                        'podcast': podcast,     
                        'news_slide': news_slide,                   
                        })
        return context



def category_video(request, id, slug):
    video_category = VideoCategory.objects.all()
    videos = Videos.objects.filter(
        category_id=id).order_by('-id')  # .order_by('id')[offset:limit]
    news_slide = NewsSlide.objects.all()[:6]

    context = {

       
        'video_category': video_category,
        'videos': videos,            
        'title': 'News Category - The Monkey Post',
        'news_slide': news_slide,

    }
    return render(request, 'video-category.html', context)


class VideoCategoryView(ListView):
    model = Videos
    template_name = 'video-category.html'
    context_object_name = 'videos'
    ordering = ['-id']
    paginate_by = 25
    

    def get_queryset(self):
        return Videos.objects.filter(category_id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    

        top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]    
        video_category = VideoCategory.objects.all()    
       
        context.update({'title': 'Videos Category - The Monkey Post',                      
                        'top_trends': top_trends,      
                        'video_category': video_category                                 
                        })
        return context





def live_view(request):
    context = {
        'title': 'Live Score - The Monkey Post',
    }
    return render(request, 'livescore.html', context)


def odds_view(request):
    context = {
        'title': 'Odds - The Monkey Post',
    }
    return render(request, 'odds.html', context)









def subscribe(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # check post
        form = SubscribeForm(request.POST)
        if form.is_valid():
            data = Subscribe()  # create relation with model # get form input data
            data.email = form.cleaned_data['email']
            data.save()
            messages.info(
                request, "Your Email has been sent. Thank you for subscribing to Shoppitza.")

            return HttpResponseRedirect(url)

    form = Subscribe()

   

    context = {

        

        's_form': form,

    }

    return HttpResponseRedirect(url)


def faq(request):
    faq = Faqs.objects.all()
   
    context = {
        'title': 'Frequently Assked Question',
        'faq': faq,
        
        
    }

    return render(request, 'faq.html', context)

def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def tandc(request):
    return render(request, 'tandc.html')


def donation(request):

    if request.method == 'POST':        
        email = request.POST.get('email', None)
        amount = request.POST.get('amount', None)
        url = 'https://api.paystack.co/transaction/initialize'
        headers = {
            'Authorization': 'Bearer sk_test_0acbc536d975b436505c7ddc7dbd1337e5b97a8e',
            'Content-Type': 'apllication/json',
            'Accept': 'application/json',
        }
        cash = {
            "email": email,
            "amount": amount*100
        }
        x = requests.post(url, data=json.dumps(cash), headers=headers)
        # print(x.status_code)
        results = x.json()
        # print('results: ', results)
        # link = []
        # print(x.json())
        # print(x['data']['authorization_url'])
        link = results['data']['authorization_url']
        

        return HttpResponseRedirect(link)

    return render(request, 'donate.html')



def contact(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data1 = form.cleaned_data
            data = ContactMessage()  # create relation with model
           
            data.phone = form.cleaned_data['phone']  # get form input data
            data.email = form.cleaned_data['email']
            data.description = form.cleaned_data['description']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(
                request, "Message sent. The Monkey Post will get back to you shortly. Thank You")
            # template = render_to_string('booking_template.html', {
            #                             'name': data1['name'],
            #                             'phone': data1['phone'],
            #                             'email': data1['email'],
            #                             'subject': data1['subject'],
            #                             'description': data1['description'],
            #                             'date': data1['date'], })

            # email = EmailMessage(
            #     'You have a new Booking! ',
            #     template,
            #     settings.EMAIL_HOST_USER,
            #     ['ceasarplusplus@gmail.com']

            # )


            # email.fail_silently = False
            # email.send()

            return HttpResponseRedirect(url)
    
    form = ContactForm()
   
    context = {
        'title': 'Contact the Monkey Post - Monkey Pos',

        
        'form': form,
       
    }

    return render(request, 'contact-us.html', context)


def about_us(request):
    

    context = {
        'title': 'About the Monkey Post - Monkey Post',
       
    }

    return render(request, 'about.html', context)



def handler400(request, exception):
    return render(request, '400.html', status=400)

def handler403(request, exception):
    return render(request, '403.html', status=400)


def handler404(request, exception):
    return render(request, '404.html', status=400)


def handler500(request):
    return render(request, '500.html', status=400)


class VideosTestView(ListView):
    model = Videos
    template_name = 'videostest.html'
    context_object_name = 'videos'
    ordering = ['-id']

    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_category = VideoCategory.objects.all()
        podcast = Videos.objects.filter(podcast=True)
        news_slide = NewsSlide.objects.all()[:6]
        context.update({'video_category': video_category,
                        'podcast': podcast,     
                        'news_slide': news_slide,                   
                        })
        return context


class Youtube(View):
    def get(self, request):
        visible = 3 
        num_posts = self.kwargs.get('num_posts')
        upper = num_posts
        lower = upper - visible
        size = Videos.objects.all().count()
        qs = Videos.objects.all().order_by('-id')
        data = serializers.serialize('json', qs)
        return JsonResponse({'data': data[lower:upper], 'size': size}, safe=False)

    

def vid_json(request, num_posts):
    visible = 3 
    upper = num_posts
    lower = upper - visible
    size = Videos.objects.all().count()
    qs = Videos.objects.all()
    data = []
    for rs in qs:
        item ={
            'id': rs.id,
            'title': rs.title,
            'link': rs.link,
            'image': rs.image.url,

        }
        data.append(item)
        
    return JsonResponse({'data': data[lower:upper], 'size': size})