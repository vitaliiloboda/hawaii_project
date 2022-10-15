from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/meeting/camera/(?P<meeting_id>\w+)/$', consumers.VideoConsumer.as_asgi()),
    re_path(r'ws/meeting/projector/(?P<meeting_id>\w+)/$', consumers.VideoConsumer.as_asgi()),
    re_path(r'ws/meeting/distant/(?P<meeting_id>\w+)/$', consumers.VideoConsumer.as_asgi()),
]
