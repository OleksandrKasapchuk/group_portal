from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_datetime = models.DateTimeField(null=False, blank=False)
    end_datetime = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title

    def clean(self):
        if self.start_datetime and self.start_datetime < timezone.now():
            raise ValidationError('Start datetime cannot be in the past.')
        if self.end_datetime and self.end_datetime < timezone.now():
            raise ValidationError('End datetime cannot be in the past.')
        if self.end_datetime and self.start_datetime and self.end_datetime < self.start_datetime:
            raise ValidationError('End datetime cannot be before start datetime.')
