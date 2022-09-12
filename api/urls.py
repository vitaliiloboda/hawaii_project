from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet, MeetingImagesViewSet, UsersInMeetingViewSet, MeetingCreate, MeetingUpdate, \
    MeetingDelete, MeetingImagesCreate, MeetingImagesDelete, MeetingImagesUpdate, UsersInMeetingCreate, \
    UsersInMeetingDelete, UsersInMeetingUpdate

app_name = 'api'

router = DefaultRouter()
router.register('meetings', MeetingViewSet, basename='meetings')
router.register('images', MeetingImagesViewSet, basename='images')
router.register('users-in-meeting', UsersInMeetingViewSet, basename='users-in-meeting')

urlpatterns = [
    path('', include(router.urls)),
    path('meeting/create/', MeetingCreate.as_view()),
    path('meeting/update/<int:pk>', MeetingUpdate.as_view()),
    path('meeting/delete/<int:pk>', MeetingDelete.as_view()),
    path('images/create/', MeetingImagesCreate.as_view()),
    path('images/update/<int:pk>', MeetingImagesUpdate.as_view()),
    path('images/delete/<int:pk>', MeetingImagesDelete.as_view()),
    path('users-in-meeting/create/', UsersInMeetingCreate.as_view()),
    path('users-in-meeting/update/<int:pk>', UsersInMeetingUpdate.as_view()),
    path('users-in-meeting/delete/<int:pk>', UsersInMeetingDelete.as_view()),
]
