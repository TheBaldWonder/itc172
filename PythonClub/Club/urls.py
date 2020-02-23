from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetails'),
    path('events/', views.events, name='events'),
    path('eventdetail/<int:id>', views.eventdetail, name='eventdetail'),
    path('resources/', views.resources, name='resources'),
    path('resourcedetail/<int:id>', views.resourcedetail, name='resourcedetail'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('newEvent/', views.newEvent, name='newevent'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]