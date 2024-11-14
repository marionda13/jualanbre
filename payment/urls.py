from django.urls import path

from . import views
# urls.py


urlpatterns = [

    path('checkout', views.checkout, name='checkout'),


    path('complete-order', views.complete_order, name='complete-order'),

    path('midtrans/', views.redirect_to_midtrans, name='midtrans'),

    path('payment-success', views.payment_success, name='payment-success'),

    path('payment-failed', views.payment_failed, name='payment-failed'),

]








