"""
Defines (very often periodic) tasks run by Celery

Author: Jakub Svoboda
Date:   08/2023
Email:  jakub.svoboda.developer@gmail.com
"""

import logging
import requests

from celery import shared_task
from .models import Video


METADATA_SOURCE = 'https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json'
METADATA_PULL_TIMEOUT = 20  # In seconds

logger = logging.getLogger(__name__)

@shared_task
def metadata_pull():
    """
    Pulls a .json file containning metadata from a remote source. 
    This JSON is then converted into Video objects which are used 
    to update local database.
    """
    try:
        response = requests.get(METADATA_SOURCE,timeout = METADATA_PULL_TIMEOUT )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        logger.error('Failed to fetch metadata: %s', exc)
        return

    for video_data in data:
        try:
            video, created = Video.objects.update_or_create(name=video_data['name'],
                                                            defaults=video_data)
            if not created:
                logger.info('Updated video: %s', video.name)
            else:
                logger.info('New video added to database: %s', video.name)

        except Exception as exc:
            logger.error('Error processing video %s: %s', video_data['name'], exc)
        