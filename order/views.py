from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as u_login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_list_or_404, get_object_or_404
from home.forms import OrderForm
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
from .models import OrderProductBack, OrderProduct, OrderBack, Order
from home.models import Setting
from news.models import  Blog, BlogCategory
from store.models import Category, Product, Images, ShopCart, ShopCartForm
from order.models import OrderProduct, Order
from users.models import Userprofile

# Create your views here.


@login_required(login_url='/login')
def checkout(request):
    url = request.META.get('HTTP_REFERER')
    setting = Setting.objects.get(pk=1)
    blog_category = BlogCategory.objects.all()
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)

        if form.is_valid():

            data = Order()
            payment_option = form.cleaned_data.get('payment_option')
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(8).upper()  # random cod
            data.code = ordercode
            data.save()

            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id  # Order Id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()

            if payment_option == 'C':

                return render(request, 'card-payment.html', {'orderid': data.id, 'total': total, 'title': 'Paystack Payment', 'blog_category': blog_category})
            else:
                return render(request, 'bank-payment.html', {'orderid': data.id, 'total': total, 'title': 'Bank Payment', 'blog_category': blog_category})

        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(url)

    form = OrderForm()
    profile = Userprofile.objects.get(user_id=current_user.id)

    context = {'shopcart': shopcart,
               'title': 'Checkout',
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               'setting': setting,
               'blog_category': blog_category,
               }
    return render(request, 'checkout.html', context)


def paystack(request, pk):
    orderid = pk
    order = Order.objects.get(pk=orderid)
    amount = int(order.total)
    print(order.total)
    url = 'https://api.paystack.co/transaction/initialize'
    headers = {
        'Authorization': 'Bearer sk_test_0acbc536d975b436505c7ddc7dbd1337e5b97a8e',
        'Content-Type': 'apllication/json',
        'Accept': 'application/json',
    }
    cash = {
        "email": request.user.email,
        "amount": amount*100
    }
    x = requests.post(url, data=json.dumps(cash), headers=headers)
    print(x.status_code)
    results = x.json()
    print('results: ', results)
    # link = []
    print(x.json())
    # print(x['data']['authorization_url'])
    link = results['data']['authorization_url']
    order.ref_code = results['data']['reference']
    order.save()

    return HttpResponseRedirect(link)


def order_completed(request):
    if(request.GET.get('trxref') != None):
        trxref = request.GET.get('trxref')
        

        print(trxref)

        paid = Order.objects.get(ref_code=trxref)
        # print('paid product', paid.product)
        # print('ref code = ', paid.ref_code)

        # books = OrderBack()

        # books.first_name = paid.first_name
        # books.last_name = paid.last_name
        # books.address = paid.address
        # books.phone = paid.phone
        # books.user_id = paid.user.id
        # books.state = paid.state
        # books.city = paid.city
        # books.ip = paid.ip
        # books.code = paid.code
        # books.ref_code = paid.ref_code
        # books.total = paid.total
        # books.ordered = True
        paid.save()
        current_user = request.user
        ShopCart.objects.filter(user_id=current_user.id).delete()
        request.session['cart_items'] = 0

        # template = render_to_string('order_template.html', {
        #                                 'name': paid.first_name,
        #                                 'phone': paid.last_name,
        #                                 'email': paid.user.email,
        #                                 'subject': data1['subject'],
        #                                 'description': data1['description'],
        #                                 'date': data1['date'], })

        #     email = EmailMessage(
        #         'You have a new Booking! ',
        #         template,
        #         settings.EMAIL_HOST_USER,
        #         ['ceasarplusplus@gmail.com']

        #     )

        #     email.fail_silently = False
        #     email.send()

    context = {
        'title': 'Order Completed - The Monkey Post',
       

    }

    return render(request, 'order-completed.html', context)

