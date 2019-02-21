from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from chat.models import Chat, Contact
from chat.views import get_user_contact
from .serializers import ChatSerializer

User = get_user_model()


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
