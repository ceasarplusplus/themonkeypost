from django.urls import path, include
from .views import shop, StoreView, StoreCategoryView, ajaxcolor, category_products, addtoshopcart, product_detail, addcomment, shopcart, addtoshopcart, deletefromcart

urlpatterns = [
    path('monkey-post-store/', StoreView.as_view(), name='shop'),
    path('shop-category/<int:id>/<slug:slug>',
         StoreCategoryView.as_view(), name='category_products'),
    path('addtoshopcart/<int:id>', addtoshopcart, name='add_to_cart'),
    path('product/<int:id>/<slug:slug>',
         product_detail, name='product_detail'),
    path('product/addcomment/<int:id>', addcomment, name='addcomment'),
    path('shopcart/', shopcart, name='shopcart'),
    path('addtoshopcart/<int:id>', addtoshopcart, name='add_to_cart'),
    path('deletefromcart/<int:id>/', deletefromcart, name='deletefromcart'),
    path('ajaxcolor/', ajaxcolor, name='ajaxcolor'),
]