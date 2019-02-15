# vue랑 django 연동하는 페이지에 있던거
# from rest_framework import serializers
# 
# from .models import Task
# 
# class TaskSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('id', 'description', 'status')

# 위에 예제 기반으로 내가 만든거
from rest_framework import serializers
# from .models import User
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'user_id', 'password', 'nickname', 'email')

# vue랑 django 연동하는 페이지에 있던거
from rest_framework import serializers
from django.contrib.auth.models import User


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username')
