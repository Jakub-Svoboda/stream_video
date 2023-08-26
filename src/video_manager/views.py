from django.db.models.functions import Lower 
from django.shortcuts import get_object_or_404, render
from .models import Video

def index(request):
    sort_order = request.GET.get('sort', 'asc')   
    if sort_order == 'asc':
        videos = Video.objects.all().order_by(Lower('name'))
    else:
        videos = Video.objects.all().order_by(Lower('name').desc())

    context = {
        'videos': videos,
        'sort_order': sort_order
    }
    return render(request, 'video/video_list.html', context)

def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    context = {
        'video': video
    }
    return render(request, 'video/detail.html', context)
