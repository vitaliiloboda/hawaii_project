from pprint import pprint

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class CameraConsumer(WebsocketConsumer):
    """ Консьюмер, получающий данные от пользователя, запустившего приложение в режиме камеры

    """

    def connect(self):

        self.meeting_id = self.scope['url_routes']['kwargs']['meeting_id']
        self.camera_group_name = f'camera_{self.meeting_id}'
        self.projector_group_name = f'projector_{self.meeting_id}'
        self.distant_group_name = f'distant_{self.meeting_id}'

        async_to_sync(self.channel_layer.group_add)(self.camera_group_name, self.channel_name)

        self.accept

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(self.camera_group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):

        pass


class ProjectorConsumer(WebsocketConsumer):
    """ Консьюмер, получающий данные от пользователя, запустившего приложение в режиме проектора

    """
    def connect(self):
        self.meeting_id = self.scope['url_routes']['kwargs']['meeting_id']
        self.group_name = f'camera_{self.meeting_id}'

        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        pass


class DistantConsumer(WebsocketConsumer):
    """ Консьюмер, получающий данные от пользователя, запустившего приложение в удаленном режиме

    """

    def connect(self):
        pprint(self.channel_layer)
        pprint(self.scope['user'].__dict__)
        self.meeting_id = self.scope['url_route']['kwargs']['meeting_id']
        self.camera_group_name = f'camera_{self.meeting_id}'
        self.projector_group_name = f'projector_{self.meeting_id}'
        self.distant_group_name = f'distant_{self.meeting_id}'

        async_to_sync(self.channel_layer.group_add)(self.camera_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        pprint(close_code)
        async_to_sync(self.channel_layer.group_discard)(self.camera_group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        pass
