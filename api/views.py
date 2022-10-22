from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import MeetingSerializer, MeetingImagesSerializer, UsersInMeetingSerializer
from meeting.models import Meeting, MeetingImages, UsersInMeeting
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


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


class MeetingEnd(APIView):
    # if uncommented any user has access to API
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk):
        meeting_id = pk
        meeting = get_object_or_404(Meeting, pk=meeting_id)
        meeting.end_meeting()
        return Response(status=status.HTTP_200_OK)
