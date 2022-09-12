from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import MeetingSerializer, MeetingImagesSerializer, UsersInMeetingSerializer
from meeting.models import Meeting, MeetingImages, UsersInMeeting
from rest_framework import permissions


class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


class MeetingCreate(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]


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
