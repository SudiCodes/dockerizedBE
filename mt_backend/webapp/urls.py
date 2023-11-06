from django.urls import path, include
from webapp.views import home_view, TitleViewset, WatchVideoView
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("home", home_view),
    path('watch/<int:title_id>/', WatchVideoView.as_view(), name='watch_video'),
    path('titles', TitleViewset.as_view({'get': 'list',
                                         'post': 'create'}))
]
