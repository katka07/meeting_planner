from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Room(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return self.name