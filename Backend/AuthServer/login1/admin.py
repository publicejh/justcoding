from django.contrib import admin
# 아래는 책 보고 따라한 것. admin 사이트에 테이블 반영하기 위해서
# from .models import User
#
#
# # Register your models here.
# admin.site.register(User)


# User 모델 확장한 후에 한국인 개발자 분이 올린거 보고 쓴거
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from .models import Profile
#
#
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline, )
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
