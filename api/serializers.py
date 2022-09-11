from rest_framework import serializers
from .models import Meeting, MeetingImages, UsersInMeeting, User


class MeetingSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Meeting
        fields = ('id', 'owner', 'url', 'start_time', 'end_time', 'name')


class MeetingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeetingImages
        fields = ('id', 'meeting', 'image')  # if needed all fields '__all__'


class UsersInMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersInMeeting
        fields = ('id', 'role', 'meeting', 'user')

