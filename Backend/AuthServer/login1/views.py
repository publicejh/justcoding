from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# django랑 vue 연동을 위한 해외 글 보고 적는 것
#
# from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
#
# class SignupViewSet(viewsets.ModelViewSet): # Create a class based view
#     """
#     API endpoint that allows tasks to be viewed or edited.
#     """
#     authentication_classes = (BasicAuthentication,)


# 초보몽키의 개발블로그-django 회원가입 구현
#
# from django.views.generic import


# 실전편 책에서
from django.views.generic.base import TemplateView

# from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
# from django.core.urlresolvers import reverse_lazy
#
#
# # User Creation
# class UserCreateView(CreateView):
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('register_done')



# simplebetterthancomplex signup
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate

#
# def signup(request):
#     if request.method=='POST':


# vue+django
from rest_framework import viewsets
#
# # 기본편 책
# def signup(request):
#     if request.method == 'POST':
#         email=get_object_or_404()

# def signup(request, email, password, nickname):
#     email = get_object_or_404(User, )

from .models import User
from .serializers import PersonSerializer
from django.apps import AppConfig
# from .managers import PersonManager


class Login1Config(AppConfig):
    name = 'login1'


class PersonViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PersonSerializer

    class Meta:
        proxy = True
        ordering = ('-username',)

    def do_print(self):
        for username in self.objects:
            print("Hello! " + username.__str__())
