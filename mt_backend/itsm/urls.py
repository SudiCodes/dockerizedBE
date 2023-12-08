from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from itsm.views import IncidentViewSet, SearchView, DummyViewSet


# Write your URLs here
router = DefaultRouter()
router.register(r'tickets', IncidentViewSet)
router.register(r'search', DummyViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', SearchView.as_view()),

]
