from django.db import models
from django.conf import settings


class Band(models.Model):
    band_name = models.CharField(max_length=45)
    band_leader = models.IntegerField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BandParticipate')

    def __str__(self):
        return self.band_name


class BandParticipate(models.Model):
    band = models.ForeignKey('sig.Band', on_delete=models.DO_NOTHING)
    is_band_leader = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)