from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BandList.as_view()),
    path('<int:pk>/', views.BandDetail.as_view()),
    path('<int:pk>/member', views.BandMemberDetail.as_view()),
    path('create/', views.BandCreate.as_view()),
]