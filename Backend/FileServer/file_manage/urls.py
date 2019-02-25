from django.urls import path, include
from .views import ImageInfoCreateView, ChatImageUploadView


urlpatterns = [
    path('upload/image/', ImageInfoCreateView.as_view()),
    path('chat/upload/image/', ChatImageUploadView.as_view()),
]
