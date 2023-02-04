from django.urls import path, include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('/about', about, name='about'),
    path('/contact', contact, name='contact'),
    url(r'^services/(?P<pk>[0-9]+)/$', services, name='services')
    # path('/services', services, name='services')
]