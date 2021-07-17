from django.urls import path, include
from django.conf.urls import url
from . import views
import re

app_name='store'
urlpatterns = [
    #path('', views.index, name='index'),
    #url(r'^$', views.index),
    path('', views.listing, name='listing'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),

]
