from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Meeting(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='meeting name',
        default='random_meeting'
    )
    owner = models.ForeignKey(
        User,
        related_name='owned_meetings',
        on_delete=models.CASCADE,
        verbose_name='meeting owner'
    )
    start_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='meeting start time'
    )
    end_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='meeting end time'
    )
    password = models.CharField(
        max_length=50,
        verbose_name='meeting password',
        default='mypassword'
    )
    users = models.ManyToManyField(
        User,
        related_name='meetings',
    )
    camera_occupied = models.BooleanField(
        default=False,
    )
    projector_occupied = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name

    def end_meeting(self):
        self.end_time = datetime.now()
        self.save()
        