from django import forms
from .models import Event
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class EventForm(forms.ModelForm):
    start_time = forms.TimeField(label='Start Time', widget=forms.TimeInput(attrs={'class': 'form-control'}))
    end_time = forms.TimeField(label='End Time', widget=forms.TimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_datetime', 'end_datetime', 'start_time', 'end_time']
        widgets = {
            'start_datetime': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
            'end_datetime': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get("start_datetime")
        end_datetime = cleaned_data.get("end_datetime")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if not start_datetime:
            self.add_error('start_datetime', 'Start datetime is required.')

        if not end_datetime:
            self.add_error('end_datetime', 'End datetime is required.')

        if not start_time:
            self.add_error('start_time', 'Start time is required.')

        if not end_time:
            self.add_error('end_time', 'End time is required.')

        if start_datetime and end_datetime and end_datetime < start_datetime:
            self.add_error('end_datetime', 'End datetime cannot be before start datetime.')