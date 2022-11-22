from django.db import models


class MeetingImages(models.Model):
    meeting = models.ForeignKey(
        'meeting.Meeting',
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