from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from meeting.models import Meeting, MeetingImages, UsersInMeeting, User


class MeetingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ('id', 'owner', 'name', 'password')


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ('__all__')


class MeetingImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeetingImages
        fields = ('id', 'meeting', 'image')  # if needed all fields '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UsersInMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersInMeeting
        fields = ('id', 'role', 'meeting', 'user')

        validators = [
            UniqueTogetherValidator(
                queryset=UsersInMeeting.objects.exclude(role=2),
                fields=['meeting', 'role']
            )
        ]

