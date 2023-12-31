"""
Configures celery tasks for video_manager.

Author: Jakub Svoboda
Date:   08/2023
Email:  jakub.svoboda.developer@gmail.com
"""

from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer, VideoInputSerializer, ValidateDataMixin


class VideoViewSet(ValidateDataMixin, viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class_out = VideoSerializer
    serializer_class_in = VideoInputSerializer

    def get_queryset(self):
        queryset = self.queryset
        validated_data = self.get_validate_data()
        name = validated_data.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        disabled = validated_data.get('disabled')
        if disabled is not None:
            queryset = queryset.filter(disabled=disabled)

        return queryset


def index(request):
    """
    View of the main page containing a list of videos.
    Args:
        request: passed request
    Returns:
        HttpResponse: rendered http response with filled context
    """
    sort_order = request.GET.get('sort', 'asc')
    search_query = request.GET.get('search')

    videos = Video.objects.all()

    if sort_order == 'asc':
        videos = videos.order_by(Lower('name'))
    else:
        videos = videos.order_by(Lower('name').desc())

    if search_query:
        videos = videos.only('name').filter(Q(name__icontains=search_query))

    context = {
        'videos': videos,
        'sort_order': sort_order,
        'search_query': search_query
    }
    return render(request, 'video/video_list.html', context)


def detail(request, video_id):
    """
    A view if a single video with detail (and TODO playback)
    Args:
        request: passed request
        video_id (int): primary key of the database object
    Returns:
       HttpResponse: rendered http response with filled context
    """
    video = get_object_or_404(Video, pk=video_id)
    context = {
        'video': video
    }
    return render(request, 'video/detail.html', context)
