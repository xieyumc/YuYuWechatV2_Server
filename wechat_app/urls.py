# wechat_app/urls.py

from django.urls import path
from .views import send_message

urlpatterns = [
    path('send_message/', send_message, name='send_message'),
]