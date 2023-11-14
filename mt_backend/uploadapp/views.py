from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, MultiPartParserError
from uploadapp.serilizers import FileSerilizer, ImageFileSerializer
from rest_framework import status
# Create your views here.


class FileView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = FileSerilizer(data=request.data)
        # print(request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            print(e)
            return Response({"Error": "Something went wrong"})


class ImageFileView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = ImageFileSerializer(data=request.data)
        # print(request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"Error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
