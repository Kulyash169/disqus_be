"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include,url
from tastypie.api import Api
from core_app.api import *
from django.contrib import admin

#set urls
v1_api = Api(api_name='v1')
v1_api.register(CommentResource())
admin.autodiscover()

urlpatterns = patterns('',
	(r'^api/', include(v1_api.urls)),
	(r'^admin/',include(admin.site.urls)),
)