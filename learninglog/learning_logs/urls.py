"""define models of URL adresses for learning_logs"""

from django.conf.urls import url
from . import views

urlpatterns = [
    #main page
    url(r'^$', views.index, name='index'),
    #showing all topics
    url(r'^topics/$', views.topics, name='topics'),
    #page with details for chosen topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #website for adding new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #webstite for adding new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,
    name='new_entry'),
    #webstite for editing entries
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    name='edit_entry'),
]
