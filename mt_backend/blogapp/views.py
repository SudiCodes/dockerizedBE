from django.shortcuts import render
from blogapp.models import Blog, Comment
from blogapp.serilizers import BlogSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class BlogView(ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serialized_data = self.serializer_class(queryset, many=True)
    #     context = {"key": "value"}
    #     return render(request, 'blog_base.html', context=context)


class CommentView(ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
