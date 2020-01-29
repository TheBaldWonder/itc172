from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('events/', views.events, name='events'),
    path('eventdetails/<int:id>', views.eventdetails, name='eventdetails'),
    path('resources/', views.resources, name='resources'),
    path('resourcedetail/<int:id>', views.resourcedetail, name='resourcedetail'),
]