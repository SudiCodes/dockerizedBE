from django.urls import path
from uploadapp.views import ImageFileView, FileView

urlpatterns = [
    path('file/', FileView.as_view()),
    path('image/', ImageFileView.as_view())
]
