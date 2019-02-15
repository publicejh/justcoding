"""django_jwt_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from django.contrib import admin
from django.urls import path, include

# 실전편 책에서
from django.conf.urls.static import static
from django.conf import  settings

#
# from django_jwt_exam.views import UserCreateView, UserCreateDoneTV

# simplebetterthancomplex signup
# from login1 import views as login1_views

# 유튜브 링크 4
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers
# from Backend.AuthServer import login1
from login1.views import PersonViewSet

# from ..login1.views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'', PersonViewSet)

urlpatterns = [
    # 이거는 다른 링크
    # url(r'^auth-jwt/', obtain_jwt_token),
    # url(r'^auth-jwt-refresh/', refresh_jwt_token),
    # url(r'^auth-jwt-verify/', verify_jwt_token),


    path('admin/', admin.site.urls),


    # 유튜브 링크 1 or 2
    # path('', include('languages.urls')),

    # JWT
    # 유튜브 링크 3
    # path('api-auth/', include('rest_framework.urls')),

    # JWT
    # 유튜브 링크 4
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),

    #url('',)

    # 실전편
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    # url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    # simplebetterthancomplex signup
    # path('/', login1_views.signup, name='signup')

    # vue + django
    path('', include(router.urls)),
]

# 유튜브 4에서 건드린 것: settings.py, urls.py, views.py, send.py

