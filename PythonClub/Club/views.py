from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Meeting, Resource, Event
from django.http import HttpResponseNotModified
from .forms import MeetingForm, ResourceForm, EventForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def index (request):
    return render(request, 'Club/index.html')

def meetings(request):
    meetings=Meeting.objects.all()
    return render(request, 'Club/meetings.html' , {'meetings': meetings})

def meetingdetail(request, id):
    meetingdetail=get_object_or_404(Meeting, pk=id)
    return render(request, 'Club/meetingdetail.html', {'meetings' : meetings})
    
def events(request):
    events_list=Event.objects.all()
    return render(request, 'Club/events.html', {'events_list': events_list})    

def eventdetail(request, id):
    event=get_object_or_404(Event, pk=id)
    return render(request, 'Club/eventdetail.html', {'event' : event})

def resources(request):
    resources_list=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resources_list': resources_list})

def resourcedetail(request, id):
    resource=get_object_or_404(Resource, pk=id)
    return render(request, 'Club/resourcedetail.html', {'resource' : resource})
