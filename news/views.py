
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
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


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

from .models import Blog, BlogComment, BlogCategory, Gif, BlogForm, NewsSlide
from home.models import Setting, Breadcrumb
from store.models import ShopCart, Comment, CommentForm
from order.models import OrderProduct, Order
from users.models import Userprofile
from .forms import SearchForm



class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    ordering = ['-id']
    paginate_by = 25

    # def get_queryset(self):
    #     return Blog.objects.filter(tags__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
       
        news_slide = NewsSlide.objects.all()[:6]
        top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]
       
        context.update({'title': 'Latest Football News - The monkey Post',
                        'news_slide': news_slide,         
                        'top_trends': top_trends,               
                        
                        })
        return context

# def blog(request):
 
#     blog_category = BlogCategory.objects.all()
#     news_slide = NewsSlide.objects.all()[:6]
   
#     blogs = Blog.objects.all().order_by('-id')
#     bc = Breadcrumb.objects.get(pk=1)
    

#     context = {
    
#         'blog_category': blog_category,
#         'blogs': blogs,
       
#         'title': 'Latest Football News - The monkey Post',
#         'bc': bc,
#         'news_slide': news_slide,
#     }

#     return render(request, 'blog.html', context)




class TagView(ListView):
    model = Blog
    template_name = 'blog-tags.html'
    context_object_name = 'blogs'
    ordering = ['-id']
    paginate_by = 28

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
       
        top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]
        
       
        context.update({'title': 'All Tag News',
                        
                        'top_trends': top_trends,
                        })
        return context

@cache_page(60 * 10)
def blog_detail(request,slug):
   
    blog = Blog.objects.get(slug=slug)
    top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]
    blogcat = blog.category
    rel_blog = Blog.objects.filter(category=blogcat).order_by('-id')
    comments = BlogComment.objects.filter(blog_id=blog.id).order_by('id')
    gif = Gif.objects.filter(blog_id=blog.id)
    pop_tags = Blog.tags.most_common()[:10]
    paginator = Paginator(comments, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'blog': blog,
        'rel_blog': rel_blog[:2],
        
        'title': 'News details - Monkey Post',
        'comments': comments,
        'top_trends': top_trends,
        'gif': gif,
        'pop_tags': pop_tags,
        'paged_listings': paged_listings,
    }

    return render(request, 'blog-details.html', context)
# @cache_page(60 * 10)
# def blog_detail(request, id, slug):
   
#     blog = Blog.objects.get(pk=id)
#     top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]
#     blogcat = blog.category
#     rel_blog = Blog.objects.filter(category=blogcat).order_by('-id')
#     comments = BlogComment.objects.filter(blog_id=id).order_by('id')
#     gif = Gif.objects.filter(blog_id=id)
#     pop_tags = Blog.tags.most_common()[:10]
#     paginator = Paginator(comments, 2)
#     page = request.GET.get('page')
#     paged_listings = paginator.get_page(page)


#     context = {
#         'blog': blog,
#         'rel_blog': rel_blog[:2],
        
#         'title': 'News details - Monkey Post',
#         'comments': comments,
#         'top_trends': top_trends,
#         'gif': gif,
#         'pop_tags': pop_tags,
#         'paged_listings': paged_listings,
#     }

#     return render(request, 'blog-details.html', context)


class BlogCategoryView(ListView):
    model = Blog
    template_name = 'blog-category.html'
    context_object_name = 'blogs'
    ordering = ['-id']
    paginate_by = 25
    

    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs.get('id')).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    

        top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]        
       
        context.update({'title': 'News Category - The Monkey Post',                      
                        'top_trends': top_trends,                                       
                        })
        return context


@cache_page(60 * 10)
def category_blog(request, id, slug):

   
    blog_category = BlogCategory.objects.all()
    
    top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]
    blogs = Blog.objects.filter(
        category_id=id).order_by('-id')  # .order_by('id')[offset:limit]

    context = {

        'blogs': blogs,
        
        'top_trends': top_trends,
        'blog_category': blog_category,
        'title': 'News Category - The Monkey Post',

    }
    return render(request, 'blog-category.html', context)



def addblogcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    # return HttpResponse(url)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            data = BlogComment()
            data.comment = form.cleaned_data['comment']

            data.blog_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(
                request, "Your comment has been posted.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


@login_required(login_url='/login')  # Check login
def deleteblogcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    BlogComment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.info(request, 'Comment deleted..')
    return HttpResponseRedirect(url)


@cache_page(60 * 15)
def highlights(request): 
    

    top_trends = Blog.objects.filter(top_news=True).order_by('-id')[:4]
        
    context = {
        'top_trends': top_trends
    }

    return render(request, 'highlights.html', context)

    
@cache_page(60 * 15)  
def highlight_json(request):
    vids = {} 
    videos = {}
    # results = {}
    highlight = []
    url = 'https://www.scorebat.com/video-api/v1/'
    r = requests.get(url)
    if r.status_code == 200:
        results = r.json()
        vids = json.dumps(results, indent=2)
        # print(vids)
        for videos in results:
            title = videos['title']
            # print('title --', title)
            competition = videos['competition']['name']
            team_a = videos['side1']['name']
            team_b = videos['side2']['name']
            embed = videos['embed']
            date = videos['date']
            thumbnail = videos['thumbnail']
            # for v in videos['videos'][:]:
            #     item = v['embed'] 
            #     print('item - ', item)
            #     vids["vid"]= item
        # print(title, competion, videos)
            vids = {
                'title': title,
                'competition': competition,
                'team_a': team_a,
                'team_b': team_b,
                'embed': embed,
                'date': date,
                'thumbnail': thumbnail,
                # 'vids': vids,
            }
            highlight.append(vids)


    
    return JsonResponse({'data': highlight})





# def highlights(request): 
#     vids = {} 
#     videos = {}
#     highlight = []
#     url = 'https://www.scorebat.com/video-api/v1/'
#     r = requests.get(url)
#     if r.status_code == 200:
#         results = r.json()
#         # vids = json.dumps(results[0], indent=2)
#         for videos in results:
#             title = videos['title']
#             # print('title --', title)
#             competiton = videos['competition']['name']
#             team_a = videos['side1']['name']
#             team_b = videos['side2']['name']
#             embed = videos['embed']
#             date = videos['date']
#             thumbnail = videos['thumbnail']
#             for v in videos['videos'][:]:
#                 item = v['embed'] 
#                 # print('item - ', item)
#                 vids["vid"]= item
#         # print(title, competion, videos)
#             videos = {
#                 'title': title,
#                 'competiton': competiton,
#                 'team_a': team_a,
#                 'team_b': team_b,
#                 'embed': embed,
#                 'date': date,
#                 'thumbnail': thumbnail,
#                 'vids': vids,
#             }
#             highlight.append(videos)
#             # for r in highlight:
#             #     print('item - ',r.title)


#         # print('highlight -- ', highlight)
#         # print()
#     context = {
#         'videos': videos,
#         'highlight': highlight,
#     }
        


#     return render(request, 'highlights.html', context)

