from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from chat.models import Contact

User = get_user_model()


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    if kwargs['created']:
        print('contact created')
        Contact.objects.create(user=instance)
