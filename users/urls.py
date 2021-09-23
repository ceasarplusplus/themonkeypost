from django.urls import path, include

from .views import login_form, register, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete, logout_view, account, user_update, user_password, user_orders, user_orderdetail

urlpatterns = [
    path('login/', login_form, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', account, name='account'),
    path('update-account/', user_update, name='user_update'),
    path('update-password/', user_password, name='user_password'),
    path('user-orders/', user_orders, name='user_orders'),
    path('order-details/<int:id>/', user_orderdetail, name='user_orderdetail'),

    path('password-reset/', PasswordReset.as_view(), name='password_reset'),

    path('password-reset/done/', PasswordResetDone.as_view(),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirm.as_view(), name='password_reset_confirm'),


    path('password-reset-complete/', PasswordResetComplete.as_view(),
         name='password_reset_complete'),
]
