from django.urls import path
from django.views import View
from .views import Index 


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    ]