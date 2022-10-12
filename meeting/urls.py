from django.urls import path
from . import views as meeting


app_name = 'meeting'

urlpatterns = [
    path('', meeting.meet, name='meet')
]
