from datetime import date
from django import forms
from django.core.exceptions import ValidationError

from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={"type": "date"}),
            'start_time': forms.TimeInput(attrs={"type": "time"}),
            'duration': forms.TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }
    
    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return d
    