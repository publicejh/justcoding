from django.urls import path, include
from . import views
from .views import FileView


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('upload/', FileView.as_view(), name='file-upload'),
    path('create/', views.PostCreateList.as_view()),
    path('comments/create', views.CommentCreate.as_view()),
    #path('<int:pk>/comments/', views.CommentView.as_view())
    #path('', include(router.urls)),
]
