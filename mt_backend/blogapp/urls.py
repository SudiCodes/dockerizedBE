from django.urls import path, include
from blogapp.views import BlogView, CommentView
from rest_framework.routers import DefaultRouter

# Write your URLs here
router = DefaultRouter()
router.register(r'blogs', BlogView)
router.register(r'comments', CommentView)

urlpatterns = [
    path('', include(router.urls))
]
