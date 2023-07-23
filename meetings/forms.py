from django import forms
from .models import Meeting, Room


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={"type": "date"}),
            'start_time': forms.TimeInput(attrs={"type": "time"}),
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
