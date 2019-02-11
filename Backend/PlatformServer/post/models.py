from django.db import models
from django.conf import settings
# from sig.models import Band

# Create your models here.
#글쓰기 모델 작성


class Post(models.Model):
    title = models.CharField(max_length=100) #게시물 제목
    content = models.TextField()  #게시물 내용
    band_id = models.ForeignKey('sig.Band', on_delete=models.DO_NOTHING)  #밴드 아이디. 자동생성되게 해야함
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True) #생성시간
    updated_at = models.DateTimeField(auto_now=True)  #업데이트 시간
    image = models.ImageField(default='media/default_image.jpeg', null=True, blank=True)  #이미지 업로드
    file = models.FileField(null=True, blank=True)  #파일업로드
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING) #유저정보 가져옴

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = [-'created_at']


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message