from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 아래는 예제
# class Task(models.Model):

#     DONE = 1
#
#     STATUS_CHOICES = (

#         (DONE, 'Done')
#     )
#
#     description = models.CharField(max_length=255)
#     status = models.IntegerField(choices=STATUS_CHOICES)

# 만들었다가 지움
# class User(models.Model):
#     user_id = models.CharField(max_length=45)
#     password = models.CharField(max_length=45)
#     nickname = models.CharField(max_length=45)
#     email = models.CharField(max_length=45)
# 
#     # 객체를 문자열로 보내주기 위해서. Admin 사이트나 장고 쉘 등에서 테이블 명을 보여주기 위해서 사용.
#     def __str__(self):
#         return self.user_id
# 

# One-to-One 확장하기
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname = models.CharField(max_length=45)
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
