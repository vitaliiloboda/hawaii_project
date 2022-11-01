from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingImagesViewSet, UsersInMeetingViewSet, MeetingCreate, MeetingUpdate, MeetingList, \
    MeetingDelete, MeetingImagesCreate, MeetingImagesDelete, MeetingImagesUpdate, UsersInMeetingCreate, \
    UsersInMeetingDelete, UsersInMeetingUpdate, UserViewSet, UserCreate, UserUpdate, UserDelete, MeetingEnd

app_name = 'api'

router = DefaultRouter()
router.register('images', MeetingImagesViewSet, basename='images')
router.register('users-in-meeting', UsersInMeetingViewSet, basename='users-in-meeting')

urlpatterns = [
    path('', include(router.urls)),
    path('meeting/create/', MeetingCreate.as_view()),
    path('meeting/list/', MeetingList.as_view()),
    path('meeting/update/<int:pk>', MeetingUpdate.as_view()),
    path('meeting/delete/<int:pk>', MeetingDelete.as_view()),
    path('user/create/', UserCreate.as_view()),
    path('user/update/<int:pk>', UserUpdate.as_view()),
    path('user/delete/<int:pk>', UserDelete.as_view()),
    path('images/create/', MeetingImagesCreate.as_view()),
    path('images/update/<int:pk>', MeetingImagesUpdate.as_view()),
    path('images/delete/<int:pk>', MeetingImagesDelete.as_view()),
    # uim = users in meeting
    path('uim/create/', UsersInMeetingCreate.as_view()),
    path('uim/update/<int:pk>', UsersInMeetingUpdate.as_view()),
    path('uim/delete/<int:pk>', UsersInMeetingDelete.as_view()),

    path('meeting/end/<int:pk>', MeetingEnd.as_view()),

]
