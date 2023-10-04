"""
Configures URL mapping for the app.

Author: Jakub Svoboda
Date:   08/2023
Email:  jakub.svoboda.developer@gmail.com
"""

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'videos', views.VideoViewSet, basename='video')

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:video_id>/", views.detail, name="detail"),
    path("api/", include(router.urls)),
]
