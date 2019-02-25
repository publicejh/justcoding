from django.contrib.auth import get_user_model
from django.db import models
import os
from sig.models import Band
from chat.models import Chat
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFill

User = get_user_model()


def set_filename_format(now, instance, filename):
    """ file format setting e.g) {username}-{microsecond}{extension} hjh-2016-07-12-158859.png """
    return '{username}-{microsecond}{extension}'.format(username=instance.user.username, microsecond=now.microsecond,
                                                        extension=os.path.splitext(filename)[1], )


def user_directory_path(instance, filename):
    """ image upload directory setting e.g)
    images/{year}/{month}/{day}/{filename} images/2016/7/12/hjh-2016-07-12-158859.png """
    now = datetime.now()
    path = 'image/{year}/{month}/{day}/{filename}'.format(year=now.year, month=now.month, day=now.day,
                                                          filename=set_filename_format(now, instance, filename), )

    return path


class ImageInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)
    photo_thumbnail = ImageSpecField(
        source='photo', 		   # 원본 ImageField 명
        processors=[Thumbnail(400, 400)], # 처리할 작업목록
        format='JPEG',		   # 최종 저장 포맷
        options={'quality': 60}  # 저장 옵션
    )


class ChatImageInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)
    photo_thumbnail = ImageSpecField(
        source='photo', 		   # 원본 ImageField 명
        processors=[Thumbnail(100, 100)], # 처리할 작업목록
        format='JPEG',		   # 최종 저장 포맷
        options={'quality': 60}  # 저장 옵션
    )
