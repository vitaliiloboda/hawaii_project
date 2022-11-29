from pprint import pprint
import base64
# from datetime import datetime

from io import BytesIO
import PIL

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Meeting


class CameraConsumer(WebsocketConsumer):
    """ Консьюмер, получающий данные от пользователя, запустившего приложение в режиме камеры

    """

    def connect(self):
        self.meeting_id = self.scope['url_route']['kwargs']['meeting_id']
        self.meeting = Meeting.objects.get(pk=self.meeting_id)
        if not self.meeting.camera_occupied:
            self.camera_connected = True
            self.camera_group_name = f'camera_{self.meeting_id}'
            # self.projector_group_name = f'projector_{self.meeting_id}'
            self.distant_group_name = f'distant_{self.meeting_id}'
            self.images = {}
            async_to_sync(self.channel_layer.group_add)(self.camera_group_name, self.channel_name)
            self.meeting.set_camera_occupied_true()
            self.accept()
            print('Подключен пользователь ' + self.scope['user'].username)
        else:
            self.accept()
            self.send(f"camera in meeting {self.meeting_id} already occupied.")

    def disconnect(self, close_code):
        if self.camera_connected:
            self.meeting.set_camera_occupied_false()
            async_to_sync(self.channel_layer.group_discard)(self.camera_group_name, self.channel_name)


    def receive(self, text_data=None, bytes_data=None):
        # pprint(text_data)
        # bdata = base64.urlsafe_b64decode(text_data.split(',')[1])
        # print(type(bdata))
        # with open(f'{datetime.now().strftime("%H-%M-%S")}.jpg', 'wb') as f:
        #     f.write(bdata)
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
        self.meeting_id = self.scope['url_route']['kwargs']['meeting_id']
        self.meeting = Meeting.objects.get(pk=self.meeting_id)
        if not self.meeting.projector_occupied:
            self.projector_connected = True
            self.meeting.set_projector_occupied_true()
            self.group_name = f'projector_{self.meeting_id}'
            self.images = {}
            async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
            self.accept()
        else:
            self.accept()
            self.send(f"projector in meeting {self.meeting_id} already occupied.")

    def disconnect(self, close_code):
        if self.projector_connected:
            self.meeting.set_projector_occupied_false()
            async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        pass

    def distant_images(self, event):
        self.images[event['channel']] = event['frame']
        images = list(self.images.values())
        # pprint(self.images.values())
        # final_image = None
        final_image = PIL.Image.new('RGBA', (800, 600), (0, 0, 0, 0))
        # final_image.save('finalstart.png')
        for i, image in enumerate(images):
            # im_arr = np.frombuffer(image, dtype=np.uint8)
            # img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
            im_file = BytesIO(image)
            img = PIL.Image.open(im_file)
            img = img.resize((800, 600))
            # img.save(f'{i}.png')
            pprint(img.__dict__)
            final_image.paste(img, (0, 0, 800, 600), img)
            # final_image.save(f'final_{i}.png')
            # if i == 0:
            #     final_image = img
            # else:
            #     final_image = cv2.addWeighted(final_image, 1, img, 1, 1)

        #     cv2.imwrite(f'{i}.png', img)
        # cv2.imwrite('1555.png', final_image)
        # _, im_arr = cv2.imencode('.png', final_image)  # im_arr: image in Numpy one-dim array format.
        # im_bytes = im_arr.tobytes()
        # final_image.save('final_final.png')
        im_file = BytesIO()
        final_image.save(im_file, format="PNG")
        im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
        # im_b64 = base64.b64encode(im_bytes)

        im_b64 = base64.b64encode(im_bytes).decode('ascii')
        self.send('data:image/png;base64,' + im_b64)


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
        byte_data = base64.urlsafe_b64decode(text_data.split(',')[1])
        # byte_data = base64.b64decode(text_data)
        # print(bdata)
        # with open(f'{datetime.now().strftime("%H-%M-%S")}.png', 'wb') as f:
        #     f.write(byte_data)

        async_to_sync(self.channel_layer.group_send)(
            self.projector_group_name,
            {
                'type': 'distant_images',
                'frame': byte_data,
                'channel': self.channel_name,
            }
        )

    def video_frame(self, event):
        frame = event['frame']
        self.send(frame)
