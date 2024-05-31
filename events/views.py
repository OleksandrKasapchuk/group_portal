from django.shortcuts import render, redirect,get_object_or_404
from .models import Event
from django.views.generic import ListView
from .forms import EventForm
from django.conf import settings
from django.template.loader import get_template

class EventsViews(ListView):
    model = Event
    template_name = 'events/event_list.html'
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
    nearest_event = events.order_by('start_datetime').first() if events.exists() else None
    farthest_event = events.order_by('-start_datetime').first() if events.exists() else None
    return render(request, 'events/event_list.html', {
        'events': events, 
        'nearest_event': nearest_event, 
        'farthest_event': farthest_event
    })

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form})

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})