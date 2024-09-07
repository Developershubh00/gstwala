# gst/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Correct the views reference here
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('gst-filing/', views.gst_filing, name='gst_filing'),
    path('payment/', views.payment, name='payment'),
]
