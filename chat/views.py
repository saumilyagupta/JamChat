from django.shortcuts import render ,redirect
from chat.models import Room, Message
from django.http import HttpResponse,JsonResponse



def home(request):
    return render(request, "home.html")

def room(request , room):
    username = request.GET['username']
    
    room_details = Room.objects.get(name = room)
    return render(request , "room.html",{
        'username': username,
        'room' : room,
        'room_details' : room_details
    })

# def checkroom(request):
#     room = request.POST['room_name']
#     username = request.POST['username']

#     if Room.objects.filter(name = room).exists():
#         return redirect('room/'+room+"/?username="+username) 
#     else :
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('room/'+room+"/?username="+username) 

def checkroom(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method", status=405)   
    try:
        room_name = request.POST['room_name']
        username = request.POST['username']
    except KeyError:
        return HttpResponse("Missing room_name or username", status=400)
    
    room, created = Room.objects.get_or_create(name=room_name)
    # return redirect(reverse('room', kwargs={'room': room.name}) + f"?username={username}")
    return redirect('room/'+room_name+"/?username="+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id= request.POST['room_id']

    new_massage = Message.objects.create(
        Value = message,
        user = username,
        Room = room_id
    )
    new_massage.save()

    return HttpResponse('Message sent')



def getMessages(request , room):
    room_details = Room.objects.get(name = room)

    message = Message.objects.filter(Room = room)
    return JsonResponse({'messages': list(message.values())})
