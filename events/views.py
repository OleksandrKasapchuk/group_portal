from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Event
from .forms import EventForm

@login_required
def add_event(request):
    if request.user.is_admin or request.user.is_moderator:
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('event_list')
        else:
            form = EventForm()
        return render(request, 'events/add_event.html', {'form': form})
    else:
        return HttpResponse("Access denied", status=403)

@login_required
def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.user.is_admin or request.user.is_moderator:
        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('event_detail', id=event.id)
        else:
            form = EventForm(instance=event)
        return render(request, 'events/edit_event.html', {'form': form})
    else:
        return HttpResponse("Access denied", status=403)

@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.user.is_admin or request.user.is_moderator:
        if request.method == 'POST':
            event.delete()
            return redirect('event_list')
        return render(request, 'events/delete_event.html', {'event': event})
    else:
        return HttpResponse("Access denied", status=403)

def event_list(request):
    events = Event.objects.filter(start_datetime__gte=now()).order_by('start_datetime')
    nearest_event = events.first() if events.exists() else None
    farthest_event = events.last() if events.exists() else None
    context = {
        'events': events, 
        'nearest_event': nearest_event, 
        'farthest_event': farthest_event
    }
    if request.user.is_authenticated:
        context['user_is_admin'] = request.user.is_admin
        context['user_is_moderator'] = request.user.is_moderator
    return render(request, 'events/event_list.html', context)

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})

class CalendarView(TemplateView):
    template_name = 'events/calendar.html'
