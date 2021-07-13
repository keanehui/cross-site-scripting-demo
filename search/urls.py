from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_index), 
    path('search/result', views.search_result),
]
