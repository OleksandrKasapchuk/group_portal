from django.contrib import admin
from django.urls import path
from events import views
from .views import EventsViews

urlpatterns = [
    path('', EventsViews.as_view(), name='event_list'),
 
]

