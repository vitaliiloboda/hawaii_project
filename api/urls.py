from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet, MeetingImagesViewSet, UsersInMeetingViewSet, MeetingCreate, MeetingUpdate, \
    MeetingDelete

app_name = 'api'

router = DefaultRouter()
router.register('meetings', MeetingViewSet, basename='meetings')

urlpatterns = [
    path('', include(router.urls)),
    path('meeting/create/', MeetingCreate.as_view()),
    path('meeting/update/<int:pk>', MeetingUpdate.as_view()),
    path('meeting/delete/<int:pk>', MeetingDelete.as_view()),
    path('images/create/', MeetingCreate.as_view()),
    path('images/update/<int:pk>', MeetingUpdate.as_view()),
    path('images/delete/<int:pk>', MeetingDelete.as_view()),
    path('users-in-meeting/create/', MeetingCreate.as_view()),
    path('users-in-meeting/update/<int:pk>', MeetingUpdate.as_view()),
    path('users-in-meeting/delete/<int:pk>', MeetingDelete.as_view()),
]
