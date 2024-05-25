import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_datetime = models.DateTimeField(null=True, blank=True) 
    end_datetime = models.DateTimeField(null=True, blank=True) 
    end_time = models.TimeField(default=datetime.time(0, 0))    

    def __str__(self):
        return self.title

    def clean(self):
        if self.start_datetime and self.start_datetime < timezone.now():
            raise ValidationError('Start datetime cannot be in the past.')
        if self.end_datetime and self.end_datetime < timezone.now():
            raise ValidationError('End datetime cannot be in the past.')


