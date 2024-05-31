from django import forms
from .models import Event
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_datetime', 'end_datetime']
        widgets = {
            'start_datetime': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
            'end_datetime': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get("start_datetime")
        end_datetime = cleaned_data.get("end_datetime")

        if not start_datetime:
            self.add_error('start_datetime', 'Start datetime is required.')

        if not end_datetime:
            self.add_error('end_datetime', 'End datetime is required.')

        if start_datetime and end_datetime and end_datetime < start_datetime:
            self.add_error('end_datetime', 'End datetime cannot be before start datetime.')
