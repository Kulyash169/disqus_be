"""This module contains API resource classes"""
from tastypie.resources import ModelResource
# from django.contrib.auth.models import User
from core_app.models import Comment
from tastypie.authorization import Authorization
# from tastypie import fields
from core_app import utils
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


#create a commentResource class
class CommentResource(ModelResource):
    class Meta:
    	limit=2000
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        filtering = {
            'currentUrl': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }