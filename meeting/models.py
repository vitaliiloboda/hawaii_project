from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Meeting(models.Model):
    name = models.CharField(max_length=200, verbose_name='meeting name', default='random_meeting')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='meeting owner')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='meeting start time')
    end_time = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=50, verbose_name='meeting password', default='mypassword')

    def __str__(self):
        return self.name

    def end_meeting(self):
        self.end_time = datetime.now()
        self.save()


class MeetingImages(models.Model):
    meeting = models.ForeignKey(
        Meeting,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='meeting'
    )
    image = models.ImageField(
        upload_to='meeting_images',
        verbose_name='meeting image',
        blank=True
    )

    def __str__(self):
        return f'{self.meeting.name} image {self.id}'


class UsersInMeeting(models.Model):
    PROJECTOR = 0
    CAMERA = 1
    GUEST = 2

    NOTE = (
        (PROJECTOR, 'projector'),
        (CAMERA, 'camera'),
        (GUEST, 'guest'),
    )

    role = models.IntegerField(
        choices=NOTE,
        verbose_name='role'
    )
    meeting = models.ForeignKey(
        Meeting,
        related_name='users',
        related_query_name='user',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='meetings',
        related_query_name='meeting',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.meeting.name} users'


class Layer(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='meeting_layers', verbose_name='meeting layer', blank=True)
