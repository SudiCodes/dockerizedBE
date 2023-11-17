from django.shortcuts import render
from blogapp.models import Blog, Comment
from blogapp.serilizers import BlogSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class BlogView(ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
