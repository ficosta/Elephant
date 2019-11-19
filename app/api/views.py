from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ChannelSerializer
from video.models import Channel



class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'felipe',

        }
        return Response(data)

    def post(self, request, *args,**kwargs):
        request.data