from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,Topic 
from .forms import RoomForm
from django.db.models import Q 
from django.contrib.auth.models import  User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
# Create your views here.
#! pk refers to the primary key of the room
# rooms = [
# {'id' : 1, 'name':  'Lets learn Python!!!'},
# {'id' : 2, 'name':  'Design With Me'},
# {'id' : 3, 'name':  'Full Stack learning'},
# ]


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try :
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User Does Not Exist')
        
        user  = authenticate(request,username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password Does Not Exist')
            
        
    context = { }
    return render(request, 'base/login_register.html',context)



def logoutUser(request):
    logout(request)
    
    return redirect('home')




def home(request):
    
    q = request.GET.get('q') if  request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q ) |
        Q(description__icontains= q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()
    
    
    
    context = {'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'base/home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)


def developers(request):
    return render(request,'developers.html')

#! a decorator to require login,redirects to login page
@login_required(login_url = 'login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')            
        
    context = {'form':form}
    return render(request, 'base/room_form.html',context)


@login_required(login_url = 'login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host :
        return HttpResponse('You are not allowed to update this room')
    
    
    if request.method == 'POST':
        form =  RoomForm(request.POST,instance= room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        

    context = {'form':form}
    return render(request,'base/room_form.html',context)



@login_required(login_url = 'login')    
def deleteRoom(request,pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html', {'obj':room})

