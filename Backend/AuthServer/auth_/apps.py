from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth_'

    def ready(self):
        from .signals import user_post_save
