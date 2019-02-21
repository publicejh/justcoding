from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact

User = get_user_model()


def get_last_20_messages(chat_id, end_at=None):
    chat = get_object_or_404(Chat, id=chat_id)
    if end_at:
        return chat.messages.filter(id__lt=end_at).order_by('-timestamp').all()[:20]
        # return chat.messages.order_by('-timestamp').all()[end_at:end_at+20]
    else:
        return chat.messages.order_by('-timestamp').all()[:20]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


def get_current_chat(chat_id):
    return get_object_or_404(Chat, id=chat_id)
