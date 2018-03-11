# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """topic recognized by user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
	    """returns models representation as string"""
	    return self.text
	    
class Entry(models.Model):
    """information about progress in learning"""
    topic = models.ForeignKey(Topic)
    text =  models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
	    verbose_name_plural = 'entries'
	
    def __str__(self):
	    """returns representation of model as string"""
	    return self.text[:50] + "..."
