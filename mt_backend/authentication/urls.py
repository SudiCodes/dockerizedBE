from authentication.views import HomeView
from django.urls import path, include


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('account/', include('djoser.urls')),
    path('login/', include('djoser.urls.jwt')),
]
