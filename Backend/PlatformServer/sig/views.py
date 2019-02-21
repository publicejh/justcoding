from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Band, BandParticipate, BandInvitationToken
from .serializers import BandSerializer, BandMemberSerializer, BandParticipateSerializer,\
    BandParticipateDetailSerializer, BandInvitationTokenSerializer
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


class BandParticipateListView(generics.ListAPIView):
    # queryset = BandParticipate.objects.all()
    serializer_class = BandParticipateDetailSerializer
    lookup_field = 'band_id'

    def get_queryset(self, **kwargs):
        band_id = self.kwargs.get(self.lookup_field, None)
        queryset = BandParticipate.objects.filter(band_id=band_id)
        return queryset.order_by('-is_band_leader')


class BandCreate(generics.CreateAPIView):
    queryset = Band
    serializer_class = BandSerializer


class BandParticipateCreateView(generics.CreateAPIView):
    queryset = BandParticipate
    serializer_class = BandParticipateSerializer
    # lookup_field = 'band_id'
    #
    # def post(self, request, *args, **kwargs):
    #     temp_dict = request.data
    #     band_id = self.kwargs.get(self.lookup_field, None)
    #     temp_dict['band_id'] = band_id
    #
    #     serializer = self.get_serializer(data=temp_dict)
    #     try:
    #         serializer.is_valid(raise_exception=True)
    #
    #         if band_id:
    #             serializer.save()
    #             return Response({'band_id': band_id})
    #         else:
    #             return Response({'error': None})
    #     except Exception as e:
    #         print('eerererere')
    #         print(e)


class BandInvitationTokenCreateView(generics.CreateAPIView):
    queryset = BandInvitationToken
    serializer_class = BandInvitationTokenSerializer


class BandInvitationTokenRetrieveView(generics.RetrieveAPIView):
    queryset = BandInvitationToken.objects.all()
    serializer_class = BandInvitationTokenSerializer
    lookup_field = 'token'

    def get_queryset(self):
        queryset = BandInvitationToken.objects.all()
        token = self.kwargs.get(self.lookup_field, None)
        return queryset.filter(token=token)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # # Perform the lookup filtering.
        # lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        #
        # assert lookup_url_kwarg in self.kwargs, (
        #         'Expected view %s to be called with a URL keyword argument '
        #         'named "%s". Fix your URL conf, or set the `.lookup_field` '
        #         'attribute on the view correctly.' %
        #         (self.__class__.__name__, lookup_url_kwarg)
        # )
        #
        # filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        # obj = get_object_or_404(queryset, **filter_kwargs)
        #
        # # May raise a permission denied
        # self.check_object_permissions(self.request, obj)

        return queryset.first()

