from django.contrib import admin
from .models import Post, Comment
# Register your models here.

#어드민 페이지에 모델을 추가
admin.site.register(Post)
admin.site.register(Comment)
