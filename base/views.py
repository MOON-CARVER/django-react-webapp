from django.shortcuts import render
from .models import Room
# Create your views here.
#! pk refers to the primary key of the room
# rooms = [
# {'id' : 1, 'name':  'Lets learn Python!!!'},
# {'id' : 2, 'name':  'Design With Me'},
# {'id' : 3, 'name':  'Full Stack learning'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)


def developers(request):
    return render(request,'developers.html')

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html',context)