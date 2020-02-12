from django.contrib import admin
from .models import Meeting, Resource, Event

# Register your models here.
# This is necessary if they are to appear in the admin app

admin.site.register(Meeting)
admin.site.register(Resource)
admin.site.register(Event) 