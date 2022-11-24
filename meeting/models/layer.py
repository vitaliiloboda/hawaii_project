from django.db import models


class Layer(models.Model):
    meeting = models.ForeignKey(
        'meeting.Meeting',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='meeting_layers',
        verbose_name='meeting layer',
        blank=True
    )
    