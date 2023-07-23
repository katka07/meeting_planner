from django.shortcuts import render, redirect, get_object_or_404
from .forms import MeetingForm, RoomForm
from .models import Meeting, Room



def meeting_detail(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})


def scheduled_meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/scheduled_meetings.html', {'meetings': meetings})


def meeting_create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save()
            return redirect('welcome')
    else:
        form = MeetingForm()
    return render(request, 'meetings/meeting_create.html', {'form': form})



def meeting_update(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'meetings/meeting_update.html', {'form': form})



def meeting_delete(request, pk):
    meeting = Meeting.objects.get(pk=pk)
    meeting.delete()
    return redirect('welcome')



def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/room_list.html', {'rooms': rooms})



def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('welcome')
    else:
        form = RoomForm()
    return render(request, 'meetings/room_create.html', {'form': form})



def room_update(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = RoomForm(instance=room)
    return render(request, 'meetings/room_update.html', {'form': form})


def room_delete(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    return redirect('welcome')
