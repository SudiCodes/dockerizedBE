from django.urls import path, include
from webapp.views import home_view, TitleViewset
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("home", home_view),
    path('titles', TitleViewset.as_view({'get': 'list',
                                         'post': 'create'}))
]
