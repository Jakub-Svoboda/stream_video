from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Video

def index(request):
    videos = Video.objects.all()
    template = loader.get_template('video/video_list.html')
    context = {
        'videos': videos
    }
    return HttpResponse(template.render(context, request))

def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    template = loader.get_template('video/detail.html')
    context = {
        'video': video
    }
    return HttpResponse(template.render(context, request))
