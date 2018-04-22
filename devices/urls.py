from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('<int:device_id>/', views.detail, name='detail'),
]
