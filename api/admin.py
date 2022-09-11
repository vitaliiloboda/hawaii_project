from django.contrib import admin
from .models import Meeting, MeetingImages, UsersInMeeting


admin.site.register(Meeting)
admin.site.register(MeetingImages)
admin.site.register(UsersInMeeting)

