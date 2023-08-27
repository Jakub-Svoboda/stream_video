"""
Defines models of the video_manager app 

Author: Jakub Svoboda
Date:   08/2023
Email:  jakub.svoboda.developer@gmail.com
"""

from django.db import models

class Video(models.Model):
    """
    Represents a single video defined by its metadata
    """
    name = models.CharField(max_length=255, unique=True)
    shortName = models.CharField(max_length=255, blank=True)
    iconUri = models.URLField()
    manifestUri = models.URLField()
    source = models.CharField(max_length=255)
    focus = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    extraText = models.JSONField(default=list)
    certificateUri = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    isFeatured = models.BooleanField(default=False)
    drm = models.JSONField(default=list)
    features = models.JSONField(default=list)
    licenseServers = models.JSONField(default=dict)
    licenseRequestHeaders = models.JSONField(default=dict)
    requestFilter = models.TextField(null=True, blank=True)
    responseFilter = models.TextField(null=True, blank=True)
    clearKeys = models.JSONField(default=dict)
    extraConfig = models.JSONField(null=True, blank=True)
    adTagUri = models.URLField(null=True, blank=True)
    imaVideoId = models.CharField(max_length=255, null=True, blank=True)
    imaAssetKey = models.CharField(max_length=255, null=True, blank=True)
    imaContentSrcId = models.CharField(max_length=255, null=True, blank=True)
    mimeType = models.CharField(max_length=255, null=True, blank=True)
    mediaPlaylistFullMimeType = models.CharField(max_length=255, null=True, blank=True)
    storedProgress = models.FloatField(default=1)
    storedContent = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
