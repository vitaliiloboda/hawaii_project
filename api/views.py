from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from requests import Response
from rest_framework import viewsets, generics
from .serializers import (MeetingSerializer,
                          MeetingCreateSerializer,
                          MeetingImagesSerializer,
                          UsersInMeetingSerializer,
                          UserSerializer)
from meeting.models import Meeting, MeetingImages, UsersInMeeting, User
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class MeetingCreate(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingCreateSerializer

    def post(self, request):
        print(self.request.user)
        request.data._mutable = True
        request.data['owner'] = str(request.user.id)
        request.data._mutable = False
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingList(ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_queryset(self):
        queryset = Meeting.objects.filter(user__user=self.request.user)
        return queryset


class MeetingRetrieve(RetrieveAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.users.filter(user=self.request.user):
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MeetingUpdate(generics.RetrieveUpdateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class MeetingDelete(generics.DestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


# class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class MeetingImagesViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingImagesSerializer
    queryset = MeetingImages.objects.all()
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class MeetingImagesCreate(generics.CreateAPIView):
    queryset = MeetingImages.objects.all()
    serializer_class = MeetingImagesSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class MeetingImagesUpdate(generics.RetrieveUpdateAPIView):
    queryset = MeetingImages.objects.all()
    serializer_class = MeetingImagesSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class MeetingImagesDelete(generics.DestroyAPIView):
    queryset = MeetingImages.objects.all()
    serializer_class = MeetingImagesSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class UsersInMeetingViewSet(viewsets.ModelViewSet):
    serializer_class = UsersInMeetingSerializer
    queryset = UsersInMeeting.objects.all()
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class UsersInMeetingCreate(generics.CreateAPIView):
    queryset = UsersInMeeting.objects.all()
    serializer_class = UsersInMeetingSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]

    # def post(self, request, format=None):
    #     return Response("ok")


    # def allowed_methods(self):
    #     """
    #     Return the list of allowed HTTP methods, uppercased.
    #     """
    #     self.http_method_names.append("post")
    #     return [method.upper() for method in self.http_method_names
    #             if hasattr(self, method)]


class UsersInMeetingUpdate(generics.RetrieveUpdateAPIView):
    queryset = UsersInMeeting.objects.all()
    serializer_class = UsersInMeetingSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class UsersInMeetingDelete(generics.DestroyAPIView):
    queryset = UsersInMeeting.objects.all()
    serializer_class = UsersInMeetingSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class MeetingEnd(APIView):
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk):
        meeting_id = pk
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        meeting.end_meeting()
        return Response(status=status.HTTP_200_OK)


class AddUserInMeeting(APIView):
    serializer_class = UsersInMeetingSerializer
    # queryset = UsersInMeeting.objects.all()

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['role', 'meeting'],
            properties={
                'role': openapi.Schema(type=openapi.TYPE_INTEGER, enum=[1, 2, 3]),
                'meeting': openapi.Schema(type=openapi.TYPE_INTEGER),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    )
    def post(self, request):
        request.data._mutable = True
        request.data['user'] = str(request.user.id)
        request.data._mutable = False
        serializer = UsersInMeetingSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            try:
                if serializer.validated_data['meeting'].password == request.data['password']:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            except KeyError:
                Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return UsersInMeeting.objects.all()
