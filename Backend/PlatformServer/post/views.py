from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import status
from django.shortcuts import redirect
from .forms import CommentForm


# Create your views here.


class PostList(generics.ListAPIView):
    # queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

    def get_queryset(self, **kwargs):
        band_id = self.request.query_params.get('bandId', None)
        queryset = Post.objects.filter(band_id=band_id)
        return queryset.order_by('-id')


class PostCreateList(generics.CreateAPIView):
    queryset = Post
    serializer_class = PostSerializer

    def create_post(request):
        if request.method == 'POST':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentCreate(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer

    # def post_new(self, request):
    #     if request.method == 'POST':
    #         serializer = PostSerializer(post, data=request.data, context={'request': request})
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST', 'DELETE'])
# def product_detail(request, pk):
#     """
#     Retrieve, update or delete a product instance.
#     """
#     try:
#         product = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(product,context={'request': request})
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = PostSerializer(product, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# def post(self, request, *args, **kwargs):
#     require_json = True
#
#     try:
#         title = self.request_json["title"]
#         content = self.request_json['content']


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def CommentView(self):
        comment = get_object_or_404(Comment, )


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = PostSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CommentListView(generics.ListAPIView):
#
#     #queryset = models.Comment.objects.filter(pk=post_id)
#     #queryset = models.Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def get_queryset(self):
#         post_id = models.Post.pk
#         return  models.Comment.objects.filter(post_id)
#여기서 post_id가 url의 숫자인 애들로 쿼리하기


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


