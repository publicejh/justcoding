from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Band
from .serializers import BandSerializer, BandMemberSerializer
from rest_framework import status
from django.contrib.auth import get_user_model


class BandList(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandMemberSerializer


class MemberList(generics.ListAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = BandMemberSerializer


class BandCreate(generics.CreateAPIView):
    queryset = Band
    serializer_class = BandSerializer

