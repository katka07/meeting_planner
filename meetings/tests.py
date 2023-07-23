import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Meeting, Room


class MeetingModelTest(TestCase):

    def test_create_meeting(self):
        meeting = Meeting.objects.create(
            title="My Meeting",
            date=datetime.date.today(),
            start_time="9:00",
            duration=60,
            room=Room.objects.create(name="My Room", floor=1, room_number=101),
        )
        self.assertEqual(meeting.title, "My Meeting")
        self.assertEqual(meeting.date, datetime.date.today())
        self.assertEqual(meeting.start_time, "9:00")
        self.assertEqual(meeting.duration, 60)
        self.assertEqual(meeting.room.name, "My Room")
        self.assertEqual(meeting.room.floor, 1)
        self.assertEqual(meeting.room.room_number, 101)

    def test_create_meeting_with_invalid_data(self):
        with self.assertRaises(ValidationError):
            Meeting.objects.create(
                title="",
                date="",
                start_time="",
                duration=0,
                room=None,
            )


class RoomModelTest(TestCase):

    def test_create_room(self):
        room = Room.objects.create(name="My Room", floor=1, room_number=101)
        self.assertEqual(room.name, "My Room")
        self.assertEqual(room.floor, 1)
        self.assertEqual(room.room_number, 101)

    def test_create_room_with_invalid_data(self):
        try:
            Room.objects.create(name="", floor=0, room_number=0)
        except ValidationError as e:
            self.assertEqual(e.message, "The name field must not be blank.")

