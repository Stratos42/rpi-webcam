from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from camera.models import CameraRoom

def index(request):
    camera_rooms = CameraRoom.objects.order_by('name')[:5]
    context = {
        'camera_list': camera_rooms,
    }
    return render(request,'cameras/index.html', context)

def camera_room(request, camera_room_id):
    camera = get_object_or_404(CameraRoom, pk=camera_room_id)
    return render(request, 'cameras/camera_room.html', {'camera': camera})
