from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as u_login, logout

from home.forms import SignUpForm, UserUpdateForm, OrderForm, SearchForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from taggit.models import Tag


from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string, get_template
# from .tokens import account_activation_token
import random
import json
from django.template import Context
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
import requests
from django.core import serializers
from .models import Userprofile
from order.models import OrderProduct, Order

# Create your views here.


def login_form(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = Userprofile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            messages.success(
                request, f"You are now logged in as {user.username}")

            return HttpResponseRedirect(url)
        else:
            messages.error(
                request, "Login Error! Username or Password is incorrect")
            return HttpResponseRedirect('/login')

        

    context = {

    }
    return render(request, 'login-register.html', context)


def register(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data = Userprofile()
            data.user_id = current_user.id
            data.image = "media/avatar.png"
            data.save()
            messages.success(request, 'Your account has been created - ' + username)

            # welcome email
            subject = "Welcome to The Monkey Post"
            to = [email]
            from_email = settings.DEFAULT_FROM_EMAIL

            ctx = {
                'username': username,
                'email': email,
            }

            message = get_template('email_welcome.html').render(ctx)
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()

            return HttpResponseRedirect('/')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(url)

    form = SignUpForm()

    context = {
        'form': form,

    }
    return render(request, 'login-register.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@ login_required(login_url='/login')
def account(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.info(
                request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/dashboard')
        else:
            messages.error(
                request, str(form.errors))
            return HttpResponseRedirect(url)
    else:
        form = PasswordChangeForm(request.user)
    current_user = request.user
    profile = Userprofile.objects.get(user_id=current_user.id)
    orders = Order.objects.filter(
        user_id=current_user.id, ordered=True).order_by('-id')
    order_product = OrderProduct.objects.filter(
        user_id=current_user.id).order_by('-id')


    context = {
        'title': current_user.username,
        'profile': profile,
        'form': form,
        'orders': orders,
      

        'order_product': order_product
    }

    return render(request, 'account.html', context)



@login_required(login_url='/login')
def user_update(request):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    if request.method == 'POST':
        # request.user is user  data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/dashboard')
    else:

       
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
       
        context = {
            'title': 'Account Update',
            
            'user_form': user_form,
            'profile_form': profile_form,
           
        }
        return render(request, 'update-account.html', context)



@login_required(login_url='/login')
def user_password(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/dashboard')
        else:
            messages.error(
                request, str(form.errors))
            return HttpResponseRedirect(url)
    else:
        
        form = PasswordChangeForm(request.user)
        return render(request, 'update-password.html', {'form': form
                                                      })


@login_required(login_url='/login')
def user_orders(request):
    
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {
               'orders': orders,
               }
    return render(request, 'user-orders.html', context)


@login_required(login_url='/login')
def user_orderdetail(request, id):
   
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)

    context = {
        
        'order': order,
        'orderitems': orderitems,
       
    }
    return render(request, 'user-order-details.html', context)


class PasswordReset(auth_views.PasswordResetView):
    template_name = 'password_reset.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category = Category.objects.all()
      
    #     context.update({'category': category,
    #                     })
    #     return context


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category = Category.objects.all()
       
    #     context.update({'category': category,
    #                     })
    #     return context


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category = Category.objects.all()
        
    #     context.update({'category': category,
    #                    })
    #     return context


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category = Category.objects.all()
        
    #     context.update({'category': category,
    #                    })
    #     return context


