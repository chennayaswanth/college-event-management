from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Event, Registration
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'  # Ensure this template exists
    context_object_name = 'events'  # You can access this in the template using {{ events }}





class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'




@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Registration.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', pk=event.id)  



class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('event_list')




@method_decorator(staff_member_required, name='dispatch')
class AdminDashboardView(ListView):
    model = Event
    template_name = 'events/admin_dashboard.html'
    context_object_name = 'events'
    ordering = ['date']




@method_decorator(staff_member_required, name='dispatch')
class EventParticipantsView(TemplateView):
    template_name = 'events/event_participants.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = self.kwargs['event_id']
        event = get_object_or_404(Event, pk=event_id)
        registrations = Registration.objects.filter(event=event)
        context['event'] = event
        context['registrations'] = registrations
        return context
