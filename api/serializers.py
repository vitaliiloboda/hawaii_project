from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from meeting.models import Meeting, MeetingImages, UsersInMeeting, User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


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
        fields = ['image']  # if needed all fields '__all__'


class UsersInMeetingForMeeting(serializers.ModelSerializer):

    class Meta:
        model = UsersInMeeting
        fields = ['user', 'role']


class MeetingRetrieveSerializer(serializers.ModelSerializer):
    images = MeetingImagesSerializer(many=True)
    users = UsersInMeetingForMeeting(many=True)

    class Meta:
        model = Meeting
        fields = ('__all__')


class UsersInMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersInMeeting
        fields = ('id', 'role', 'meeting', 'user')

        validators = [
            UniqueTogetherValidator(
                queryset=UsersInMeeting.objects.exclude(role=2),
                fields=['meeting', 'role']
            ),
            UniqueTogetherValidator(
                queryset=UsersInMeeting.objects.all(),
                fields=['meeting', 'user']
            )
        ]

