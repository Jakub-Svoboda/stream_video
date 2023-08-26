from django.db.models import Q
from django.db.models.functions import Lower 
from django.shortcuts import get_object_or_404, render
from .models import Video

def index(request):
    sort_order = request.GET.get('sort', 'asc')
    search_query = request.GET.get('search')

    videos = Video.objects.all()

    if sort_order == 'asc':
        videos = videos.order_by(Lower('name'))
    else:
        videos = videos.order_by(Lower('name').desc())

    if search_query:
        videos = videos.filter(Q(name__icontains=search_query))

    context = {
        'videos': videos,
        'sort_order': sort_order,
        'search_query': search_query
    }
    return render(request, 'video/video_list.html', context)


def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    context = {
        'video': video
    }
    return render(request, 'video/detail.html', context)
