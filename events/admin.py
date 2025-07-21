from django.contrib import admin
from .models import Event, Registration, Feedback, EventCategory

admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Feedback)
admin.site.register(EventCategory)
