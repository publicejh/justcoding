from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageInfo, ChatImageInfo
from chat.models import Message
from sig.models import Band
from .serializers import ImageInfoSerializer, ChatImageInfoSerializer
from rest_framework.parsers import (
    FileUploadParser,
    MultiPartParser,
    FormParser
)
from django.contrib.auth import get_user_model
import json
import requests

User = get_user_model()


class ImageInfoCreateView(APIView):
    queryset = ImageInfo.objects.all()
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ImageInfoSerializer

    def post(self, request, format=None, *args, **kwargs):

        file = request.FILES['file']
        user_id = request.data['userId']
        band_id = request.data['bandId']

        image_info_serializer = ImageInfoSerializer(data={'user': user_id, 'band': band_id, 'photo': file})

        if image_info_serializer.is_valid():
            image_info_serializer.save()

            return Response(image_info_serializer.data['photo_thumbnail'], status=status.HTTP_200_OK)
        else:
            return Response(image_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatImageUploadView(APIView):
    queryset = ChatImageInfo.objects.all()
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ChatImageInfoSerializer

    def post(self, request, format=None, *args, **kwargs):

        file = request.FILES['file']
        user_id = request.data['userId']
        user = User.objects.get(pk=user_id)
        chat_id = request.data['chatId']

        chat_image_info_serializer = ChatImageInfoSerializer(data={'user': user_id, 'chat': chat_id, 'photo': file})

        if chat_image_info_serializer.is_valid():
            chat_image_info_serializer.save()

            send_data = {
                'from': user.username,
                'is_file': True,
                'file_path': chat_image_info_serializer.data['photo_thumbnail'],
                'chat_id': chat_id
            }
            data_json = json.dumps(send_data)

            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}



            res = requests.post("http://localhost:8002/chat/upload/image/", data=data_json, headers=headers)
            if res.json().get('result') == 8400:  # ChatServer가 제대로 websocket을 보내지 않은 경우
                return Response({'result': 400}, status=status.HTTP_200_OK)
                # return Response({'result': status_code['CHAT_MADE_FAIL']}, status=status.HTTP_200_OK)

            return Response(chat_image_info_serializer.data['photo_thumbnail'], status=status.HTTP_200_OK)
        else:
            return Response(chat_image_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
