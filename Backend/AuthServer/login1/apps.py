from django.apps import AppConfig
from django.contrib.auth.models import User
# from .managers import PersonManager


class Login1Config(AppConfig):
    name = 'login1'


class Person(User):
    objects = User.objects.all()

    class Meta:
        proxy = True
        ordering = ('-username',)

    def do_print(self):
        for username in self.objects:
            print("Hello! " + username.__str__())
