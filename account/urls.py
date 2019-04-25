from django.urls import path
from . import  views
from django.conf.urls import url
from django.contrib.auth.views import LoginView

urlpatterns = [

    url(r'^$', views.Home),
    url(r'^login/$', LoginView.as_view(template_name='account/login.html'),name="login"),
    url(r'^Signup/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^lab/$', views.lab, name='lab'),
    url(r'^labtwo/$', views.labtwo, name='labtwo'),
    url(r'^labthree/$', views.labthree, name='labthree'),
    url(r'^labf/$', views.labf, name='labf'),
    url(r'^labfi/$', views.labfi, name='labfi'),
    url(r'^labsi/$', views.labsi, name='labsi'),
    url(r'^labse/$', views.labse, name='labse'),
    url(r'^labe/$', views.labe, name='labe'),
    url(r'^labn/$', views.labn, name='labn'),
    url(r'^labt/$', views.labt, name='labt'),

    url(r'^classroom/$', views.classroom, name='classroom'),
    url(r'^crt/$', views.crt, name='crt'),
    url(r'^crth/$', views.crth, name='crth'),
    url(r'^crf/$', views.crf, name='crf'),
    url(r'^crfi/$', views.crfi, name='crfi'),
    url(r'^crs/$', views.crs, name='crs'),

]
