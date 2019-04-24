from django.urls import path
from . import  views
from django.conf.urls import url
from django.contrib.auth.views import login,logout

urlpatterns = [

    url(r'^$', views.Home),
    url(r'^login/$', login, {'template_name':'account/login.html'}),
    url(r'^Signup/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^lab/$', views.lab, name='lab'),
    url(r'^labtwo/$', views.labtwo, name='labtwo'),
    url(r'^labthree/$', views.labthree, name='labthree'),
    url(r'^labf/$', views.labf, name='labf'),
    url(r'^labfi/$', views.labfi, name='labfi'),
    url(r'^labsi/$', views.labsi, name='labsi'),
    url(r'^labse/$', views.labse, name='labse'),
    url(r'^classroom/$', views.classroom, name='classroom'),



]
