from rest_framework import serializers
from . import models
from .models import Band


class BandSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Band


class BandMemberSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('members', 'band_leader')
        model = models.Band