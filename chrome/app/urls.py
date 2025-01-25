from django.urls import path
from . import views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)

urlpatterns=[
    path('', views.chrome_login, name='chrome_login'),
    path('chrome_logout',views.chrome_logout),

    # ----------------admin--------------------
    path('home_ad',views.home_ad),
   
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete),
    

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),





    # --------------user---------------------


    path('register/',views.register),
    path('user_home',views.user_home),
    path('view_pro/<pid>',views.view_pro),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('delete-cart/<int:id>',views.delete_cart, name='delete_cart'),
    path('user_buy/<int:pid>/', views.user_buy, name='user_buy'),

    path('user_buy1/<pid>',views.user_buy1),
    path('booking',views.booking),
    path('user_booking',views.user_booking),
    path('userprd',views.userprd),
    path('order/', views.order_page, name='order_page'),
    path('order_success/',views.order_success, name='order_success'),
    
]