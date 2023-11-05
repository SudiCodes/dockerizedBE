from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
import random
from rest_framework.viewsets import ModelViewSet

from webapp.models import Genre, CastMember, Title
from webapp.serializers import GenreSerializer, CastMemberSerializer, TitleSerializer

# Create your views here.


class TitleViewset(ModelViewSet):
    permission_classes = []
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


def home_view(request):
    context = {
        "titles": TitleSerializer(Title.objects.all(), many=True).data
    }
    # print(context["titles"])
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)
