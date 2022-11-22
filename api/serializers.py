from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from meeting.models import Meeting, MeetingImages, User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


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


class UserDataForMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class MeetingRetrieveSerializer(serializers.ModelSerializer):
    images = MeetingImagesSerializer(many=True)
    users = UserDataForMeetingSerializer(many=True)

    class Meta:
        model = Meeting
        fields = ('__all__')


class MeetingAddSelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ['id', 'users']

