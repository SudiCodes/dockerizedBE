from django.shortcuts import render
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse
import random
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


from webapp.models import Genre, CastMember, Title
from webapp.serializers import GenreSerializer, CastMemberSerializer, TitleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


class WatchVideoView(APIView):
    # Apply the decorators to disable authentication
    @authentication_classes([])  # An empty list disables authentication
    @permission_classes([AllowAny])  # Allow access to anyone
    def get(self, request, title_id):
        try:
            title = TitleSerializer(
                Title.objects.get(id=title_id), many=False).data
        except Title.DoesNotExist:
            return Response({"error": "Title not found"}, status=status.HTTP_404_NOT_FOUND)
        context = {
            "title": title
        }
        # print(title)
        return render(request, 'watch-video.html', context)
