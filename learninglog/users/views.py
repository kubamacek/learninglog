# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """registration the new user"""
    if request.method != 'POST':
        #shows empty registration form
        form = UserCreationForm()
    else:
	    #filled form should be processed
	    form = UserCreationForm(data=request.POST)
	    
	    if form.is_valid():
		    new_user = form.save()
		    #log in and go to main page
		    authenticated_user = authenticate(username=new_user.username, 
		    password=request.POST['password1'])
		    login(request, authenticated_user)
		    return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
