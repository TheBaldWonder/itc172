from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField(auto_now=False,auto_now_add=False)
    meetingtime=models.TimeField(auto_now=False,auto_now_add=False)
    location=models.TextField()
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

        class Meta:
            db_table='meeting'
            verbose_name_plural='meetings'



class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceURL=models.URLField(null=True, blank=True)
    entryDate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField()
    eventdate=models.DateTimeField(auto_now=False,auto_now_add=False)
    eventtime=models.DateTimeField(auto_now=False,auto_now_add=False)
    eventdescription=models.TextField(null=True, blank=True)
    eventURL=models.URLField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self): 
        return self.eventtitle
        
        class Meta:
            db_table='event'
            verbose_name_plural='events'   