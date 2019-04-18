from django.urls import path
from . import  views
from django.conf.urls import url
from django.contrib.auth.views import login

urlpatterns = [

    url(r'^$', views.Home),
    #url(r'^login/$', views.login, name='login'),
    url(r'^login/$', login, {'template_name':'account/login.html'}),
    url(r'^Signup/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile')

]
