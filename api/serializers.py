from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from meeting.models import Meeting, MeetingImages


class UserCreateSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        write_only_fields = ['password']


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

