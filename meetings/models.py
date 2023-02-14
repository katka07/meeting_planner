from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}: room {self.room_number} on floor {self.floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    # This will overide the object with returned name on ADMIN page.
    def __str__(self) -> str:
        return f"{self.title} at {self.start_time} on {self.date}"