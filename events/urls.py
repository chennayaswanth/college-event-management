from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    EventListView,
    EventDetailView,
    register_event,
    UserRegisterView,
    AdminDashboardView,
    EventParticipantsView,
)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/<int:event_id>/register/', register_event, name='register_event'),

    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin-dashboard/event/<int:event_id>/participants/', EventParticipantsView.as_view(), name='event_participants'),
    # Example logout URL pattern
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]