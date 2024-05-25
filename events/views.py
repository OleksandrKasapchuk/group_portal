from django.shortcuts import render, redirect
from .models import Event
from django.views.generic import ListView
from .forms import EventForm
from django.conf import settings
from django.template.loader import get_template


class EventsViews(ListView):
    model = Event
    template_name ='events/event_list.html'
    context_object_name = 'events'

def add_event(request):
    try:
        template = get_template('events/add_event.html')
    except Exception as e:
        raise Exception(f"Available template directories: {settings.TEMPLATES[0]['DIRS']}\nError: {e}")

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    nearest_event = Event.nearest_event()
    farthest_event = Event.farthest_event()
    return render(request, 'events/event_list.html', {'events': events, 'nearest_event': nearest_event, 'farthest_event': farthest_event})