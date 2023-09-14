
from django.urls import path
from . import  views
urlpatterns = [
    path('', views.scrape_data, name='index'),
    path('get', views.get_data, name='get_data')
]