from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, MultiPartParserError
from uploadapp.serilizers import FileSerilizer, ImageFileSerializer, ImageFileSerilizerUploaded
from authentication.models import Customer
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

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # The client's IP might be in a comma-separated list if your app is behind a proxy or load balancer
            ip = x_forwarded_for.split(',')[0]
        else:
            # If there's no proxy, use REMOTE_ADDR
            ip = request.META.get('REMOTE_ADDR')

        return ip

    def post(self, request):
        user_id = None
        if request.user:
            user_id = request.user.id
        else:
            return Response({"Alert": "Unauthorized upload"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ImageFileSerializer(data=request.data)

        try:
            if serializer.is_valid():
                serializer.validated_data['uploaded_by'] = Customer.objects.get(
                    id=user_id)
                serializer.validated_data["uploaded_from"] = self.get_client_ip(
                    request)
                saved_serializer = serializer.save()
                response_serializer = ImageFileSerilizerUploaded(
                    saved_serializer)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"Error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
