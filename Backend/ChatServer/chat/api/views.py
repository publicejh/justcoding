from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from chat.models import Chat, Contact, Message
from chat.views import get_user_contact, get_current_chat
from .serializers import ChatSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from chat.consumers import ChatConsumer
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()
channel_layer = get_channel_layer()


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username', None)
        band_id = self.request.query_params.get('band_id', None)
        if username is not None and band_id is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.filter(band_id=band_id)
        return queryset


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )
    # permission_classes = (permissions.IsAuthenticated, )

    # def post(self, request, *args, **kwargs):
    #     temp_dict = request.data
    #     band_id = self.kwargs.get(self.lookup_field, None)
    #     temp_dict['band_id'] = band_id
    #
    #     serializer = self.get_serializer(data=temp_dict)
    #     try:
    #         serializer.is_valid(raise_exception=True)
    #
    #         if band_id:
    #             serializer.save()
    #             return Response({'band_id': band_id})
    #         else:
    #             return Response({'error': None})
    #     except Exception as e:
    #         print('eerererere')
    #         print(e)


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatSendFileView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        print("[[ChatSend]] post")
        username = request.data['from']
        is_file = request.data['is_file']
        file_path = request.data['file_path']
        chat_id = request.data['chat_id']


        chat = Chat.objects.get(pk=chat_id)


        user_contact = get_user_contact(username)
        message = Message.objects.create(
            contact=user_contact,
            is_file=is_file,
            file_path=file_path
        )
        current_chat = get_current_chat(chat_id)
        current_chat.messages.add(message)
        current_chat.save()
        content = {
            'command': 'new_message',
            'message': message_to_json(message)
        }

        print('xxxxxxx')
        print(content)
        print(chat.group_name())

        try:
            # websocket으로 message send 하기
            async_to_sync(channel_layer.group_send)(
                chat.group_name(),
                {
                    "type": "chat_message",  # call chat_message method
                    "message": content,
                }
            )
            return Response({'result': 8200}, status=status.HTTP_200_OK)
        except Exception as ex:
            print('eeeeee')
            print(ex)
            return Response({'result': 8400}, status=status.HTTP_200_OK)


def message_to_json(message):
    return {
        'id': message.id,
        'author': message.contact.user.username,
        'content': message.content,
        'is_file': message.is_file,
        'file_path': message.file_path,
        'timestamp': str(message.timestamp)
    }
