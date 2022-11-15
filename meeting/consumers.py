from pprint import pprint
import base64
from datetime import datetime

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class CameraConsumer(WebsocketConsumer):
    """ Консьюмер, получающий данные от пользователя, запустившего приложение в режиме камеры

    """

    def connect(self):

        self.meeting_id = self.scope['url_route']['kwargs']['meeting_id']
        self.camera_group_name = f'camera_{self.meeting_id}'
        # self.projector_group_name = f'projector_{self.meeting_id}'
        self.distant_group_name = f'distant_{self.meeting_id}'

        async_to_sync(self.channel_layer.group_add)(self.camera_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(self.camera_group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        # pprint(text_data)
        bdata = base64.urlsafe_b64decode(text_data.split(',')[1])
        # print(type(bdata))
        with open(f'{datetime.now().strftime("%H-%M-%S")}.jpg', 'wb') as f:
            f.write(bdata)
        print(f'Получены данные камеры в встрече {self.camera_group_name} Отправляю пользователям {self.distant_group_name}')
        async_to_sync(self.channel_layer.group_send)(
            self.distant_group_name,
            {
                'type': 'video_frame',
                'frame': text_data
            }
        )



class ProjectorConsumer(WebsocketConsumer):
    """ Консьюмер, получающий данные от пользователя, запустившего приложение в режиме проектора

    """
    def connect(self):
        self.meeting_id = self.scope['url_routes']['kwargs']['meeting_id']
        self.group_name = f'camera_{self.meeting_id}'

        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        pass


class DistantConsumer(WebsocketConsumer):
    """ Консьюмер, получающий данные от пользователя, запустившего приложение в удаленном режиме

    """

    def connect(self):
        # pprint(self.channel_layer)
        # pprint(self.scope['user'].__dict__)
        self.meeting_id = self.scope['url_route']['kwargs']['meeting_id']
        self.camera_group_name = f'camera_{self.meeting_id}'
        self.projector_group_name = f'projector_{self.meeting_id}'
        self.distant_group_name = f'distant_{self.meeting_id}'

        async_to_sync(self.channel_layer.group_add)(self.distant_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        pprint(close_code)
        async_to_sync(self.channel_layer.group_discard)(self.camera_group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        # pprint(text_data)
        # print(type(bdata))
        # text_data = text_data + '=' * (-len(text_data) % 4)
        # print(text_data)
        bdata = base64.urlsafe_b64decode(text_data.split(',')[1])
        # bdata = base64.b64decode(text_data)
        # print(bdata)
        with open(f'{datetime.now().strftime("%H-%M-%S")}.png', 'wb') as f:
            f.write(bdata)

    def video_frame(self, event):
        print('1')
        frame = event['frame']
        self.send(frame)
