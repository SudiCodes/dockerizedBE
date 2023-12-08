from django.shortcuts import render
from rest_framework import viewsets
from itsm.models import Incident
from itsm.serilizers import IncidentSerializer, SearchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline

# Create your views here.


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class SearchView(APIView):

    def get(self, request):
        q = request.GET.get("q")

        sv = SearchVector("incident_id", "requester", "ci")
        query = SearchQuery(q)
        search_headline = SearchHeadline("requester", query)

        # res = Incident.objects.annotate(search=sv).filter(search=query)
        # res = Incident.objects.annotate(
        #     rank=SearchRank(sv, query)).filter(rank__gte=0.001).order_by("-rank")
        res = Incident.objects.annotate(rank=SearchRank(sv, query)).annotate(
            headline=search_headline).filter(rank__gte=0.001).order_by("-rank")

        serialized_data = SearchSerializer(
            res, many=True, context={"request": request}).data

        # print(res[0].rank, "\n", res[0].headline)

        return Response({"search_result": serialized_data}, status=status.HTTP_200_OK)


class DummyViewSet(viewsets.ViewSet):
    def list(self, request):
        search_view = SearchView()
        return search_view.get(request)
