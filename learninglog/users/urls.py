"""defines models of the URL adresses for users app"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #website for login
    url(r'^login/$', login, {'template_name': 'users/login.html'}, 
        name='login'),
    #website for logout
    url(r'^logout/$', views.logout_view, name='logout'),
    #website for registration
    url(r'^register/$', views.register, name='register'),
]
