from django.test import TestCase
from .models import Meeting, Event, Resource
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .forms import MeetingForm

# Create your tests here
class MeetingTest(TestCase):
    def test_stringoutput(self):
        meeting=Meeting(meetingtitle='monthly')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Club_meeting')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='gala')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Club_event')

class MeetingFormTest(TestCase):
    def setUp(self):
        
        def test_meetingFormValid(self):
            form = MeetingForm(
                data={
                    'meetingtitle' : 'meeting1', 'meetingdate' : datetime.date(2019,5,30),
                }
            )
            self.assertTrue(form.is_valid())

        def test_meetingFormMinusDescript(self):
            form = MeetingForm(
                data= {
                    'meetingtitle' : 'meeting1'
                }
            )
            self.assertFalse(form.is_valid())

        def test_meetingFormEmpty(self):
            form = MeetingForm(
                data= {
                    'meetingtitle' : ''
                }
            )
            self.assertFalse(form.is_valid())