from django.db import models
from django.conf import settings


class Band(models.Model):
    band_name = models.CharField(max_length=45)
    band_cover_img_path = models.CharField(max_length=200, default='/media/static/t1.jpeg')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BandParticipate')

    def __str__(self):
        return self.band_name


class BandParticipate(models.Model):
    band = models.ForeignKey('sig.Band', on_delete=models.CASCADE)
    is_band_leader = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('band', 'user'),)


class BandInvitationToken(models.Model):
    band = models.ForeignKey('sig.Band', on_delete=models.CASCADE)
    token = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.token
