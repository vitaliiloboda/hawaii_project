from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from requests import Response
from rest_framework import viewsets, generics
from .serializers import (
    MeetingSerializer,
    MeetingCreateSerializer,
    MeetingRetrieveSerializer,
    MeetingImagesSerializer,
    UserCreateSerializer,
    MeetingAddSelfSerializer,
    MeetingListSerializer,
)
from django.contrib.auth.models import User
from meeting.models import Meeting, MeetingImages
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# class UserViewSet(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


# class UserUpdate(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]
#
#
# class UserDelete(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]


class MeetingCreate(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingCreateSerializer

    def post(self, request):
        print(self.request.user)
        request.data['owner'] = str(request.user.id)
        request.data['users'] = [request.user.id]
        pprint(request.data)
        serializer = MeetingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingList(ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingListSerializer

    def get_queryset(self):
        queryset = Meeting.objects.filter(users=self.request.user)
        return queryset


class MeetingRetrieve(RetrieveAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # if not instance.users.filter(user=self.request.user):
        if not self.request.user in instance.users.all():
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# class MeetingUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Meeting.objects.all()
#     serializer_class = MeetingSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]
#
#
# class MeetingDelete(generics.DestroyAPIView):
#     queryset = Meeting.objects.all()
#     serializer_class = MeetingSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]


# class MeetingImagesViewSet(viewsets.ModelViewSet):
#     serializer_class = MeetingImagesSerializer
#     queryset = MeetingImages.objects.all()
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]
#
#
# class MeetingImagesCreate(generics.CreateAPIView):
#     queryset = MeetingImages.objects.all()
#     serializer_class = MeetingImagesSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]
#
#
# class MeetingImagesUpdate(generics.RetrieveUpdateAPIView):
#     queryset = MeetingImages.objects.all()
#     serializer_class = MeetingImagesSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]
#
#
# class MeetingImagesDelete(generics.DestroyAPIView):
#     queryset = MeetingImages.objects.all()
#     serializer_class = MeetingImagesSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]


# class UsersInMeetingViewSet(viewsets.ModelViewSet):
#     serializer_class = UsersInMeetingSerializer
#     queryset = UsersInMeeting.objects.all()
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]
#
#
# class UsersInMeetingUpdate(generics.RetrieveUpdateAPIView):
#     queryset = UsersInMeeting.objects.all()
#     serializer_class = UsersInMeetingSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]
#
#
# class UsersInMeetingDelete(generics.DestroyAPIView):
#     queryset = UsersInMeeting.objects.all()
#     serializer_class = UsersInMeetingSerializer
#     # if uncommented any user has access to API
#     permission_classes = [permissions.AllowAny]


class MeetingEnd(APIView):

    def post(self, request, pk):
        meeting_id = pk
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        meeting.end_meeting()
        return Response(status=status.HTTP_200_OK)


# class UsersInMeetingAdd(APIView):
#     serializer_class = UsersInMeetingSerializer
#     queryset = UsersInMeeting.objects.all()

    # @swagger_auto_schema(
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         required=['role', 'meeting'],
    #         properties={
    #             'role': openapi.Schema(
    #                 type=openapi.TYPE_INTEGER,
    #                 enum=[0, 1, 2],
    #                 description='Выбор роли: \n 0 - проектор \n 1 - камера \n 2 - онлайн пользователь'
    #             ),
    #             'meeting': openapi.Schema(type=openapi.TYPE_INTEGER),
    #             'password': openapi.Schema(type=openapi.TYPE_STRING),
    #         },
    #     ),
    # )
    # def post(self, request):
    #     request.data['user'] = str(request.user.id)
    #     serializer = UsersInMeetingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         try:
    #             if serializer.validated_data['meeting'].password == request.data['password']:
    #                 serializer.save()
    #                 return Response(serializer.data, status=status.HTTP_201_CREATED)
    #             else:
    #                 return Response(status=status.HTTP_403_FORBIDDEN)
    #         except KeyError:
    #             Response(status=status.HTTP_400_BAD_REQUEST)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddSelfInMeetingView(UpdateAPIView):
    serializer_class = MeetingAddSelfSerializer
    queryset = Meeting.objects.all()

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Метод не поддерживается',
        ),
    )
    def put(self, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['password'],
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    )
    def patch(self, request, pk):
        meeting = self.get_object()
        request.data['users'] = [request.user.id]
        for user in meeting.users.all():
            request.data['users'].append(user.id)
        if request.data.pop('password') == meeting.password:
            return self.partial_update(request, pk)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
