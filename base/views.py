from django.shortcuts import render

# Create your views here.

rooms = [
{'id' : 1, 'name':  'Lets learn Python!!!'},
{'id' : 2, 'name':  'Design With Me'},
{'id' : 3, 'name':  'Full Stack learning'},
]






def home(request):
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request):
    return render(request,'room.html')


def developers(request):
    return render(request,'developers.html')