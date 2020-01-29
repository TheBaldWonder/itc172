from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Meeting, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'Club/index.html')

def meetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html' , {'meetings_list' : meetings_list})

def meetingdetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'clubapp/meetingdetails.html', {'meeting' : meeting})
    
def events(request):
    events_list=Event.objects.all()
    return render(request, 'Club/events.html', {'events_list': events_list})    

def eventdetails(request, id):
    event=get_object_or_404(Event, pk=id)
    return render(request, 'clubapp/eventdetails.html', {'event' : event})

def resources(request):
    resources_list=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resources_list': resources_list})

def resourcedetail(request, id):
    resource=get_object_or_404(Resource, pk=id)
    return render(request, 'clubapp/resourcedetail.html', {'resource' : resource})
