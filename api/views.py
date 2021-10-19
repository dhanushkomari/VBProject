from django.shortcuts import render, resolve_url
from .serializers import VoiceSerializer, VersionSettingSerializer
from .models import Voice, VersionSetting
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from api import serializers

# Create your views here.

#####################   VOICE API VIEWS    ######################
@api_view(['GET'])
def all(request):
    v = Voice.objects.all()
    serializer = VoiceSerializer(v, many = True)
    return Response(serializer.data)

@api_view(["POST"])
def postVoice(request):
    serializer = VoiceSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = VoiceSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###################   VERSION SETTINGS VIEWS    ################

@api_view(['GET'])
def recent(request):
    try:
        v = VersionSetting.objects.latest('pk')
        serialzers = VersionSettingSerializer(v, many = False)
        return Response(serialzers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Data Found, Please add some data</center></h1>')

@api_view(['GET'])
def ByVerName(request, ver_name):
    try:
        v = VersionSetting.objects.get(version_name = ver_name)
        serializers = VersionSettingSerializer(v, many = False)
        return Response(serializers.data)
    except:
        return HttpResponse('<br><br><center><h1>No Version Found with the name</center></h1>')