from django.shortcuts import render
from django.http import HttpResponse
import socket, os

from meetings.models import Meeting


def welcome(request):
    node_name = socket.gethostbyaddr(socket.gethostname())[0]
    container_name = os.environ.get("HOSTNAME")
    return render(request, "website/welcome.html",
    {"node_name": node_name, "container_name" : container_name, "meetings": Meeting.objects.all()})