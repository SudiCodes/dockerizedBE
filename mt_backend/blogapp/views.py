from django.shortcuts import render
from blogapp.models import Blog, Comment
from blogapp.serilizers import BlogSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.response import Response

# Create your views here.


class BlogView(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all().order_by("-id")

    # (second * min * hour)
    @method_decorator(cache_page(60 * 5 * 1))
    def list(self, request):
        return Response(self.serializer_class(self.queryset, many=True).data)


class CommentView(ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
