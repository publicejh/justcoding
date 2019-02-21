from rest_framework import serializers
from .models import Band, BandParticipate, BandInvitationToken


class BandSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Band


class BandMemberSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('members', 'band_leader')
        model = Band


class BandParticipateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = BandParticipate


class BandParticipateDetailSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        fields = ('is_band_leader', 'band', 'username', )
        model = BandParticipate


class BandInvitationTokenSerializer(serializers.ModelSerializer):
    band_name = serializers.SerializerMethodField()

    def get_band_name(self, obj):
        return obj.band.band_name

    class Meta:
        fields = ('id', 'token', 'band', 'band_name', )
        model = BandInvitationToken
