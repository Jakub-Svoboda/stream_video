"""
Basic set of tests of video_manager

Author: Jakub Svoboda
Date:   08/2023
Email:  jakub.svoboda.developer@gmail.com
"""

from django.test import TestCase
from django.urls import reverse
from .models import Video

VIDEO_NAME_A = 'Test video A'
VIDEO_NAME_B = 'Test video B'
VIDEO_NAME_C = 'test video C'
VIDEO_NAME_D = 'T3st video D'


class VideoViewTestCase(TestCase):
    """
    Test cases of the video_managers view methods.
    """
    def setUp(self):
        self.video1 = Video.objects.create(name=VIDEO_NAME_A,
                                           iconUri="http://example.com/icon1.png")
        self.video2 = Video.objects.create(name=VIDEO_NAME_B,
                                           iconUri="http://example.com/icon2.png")
        self.video3 = Video.objects.create(name=VIDEO_NAME_C,
                                           iconUri="http://example.com/icon3.png")

    def test_index_view(self):
        """
        Main page should return OK code and have a video
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, VIDEO_NAME_A)

    def test_sorted_index_view(self):
        """
        Test a descending sort order of videos
        """
        response = self.client.get(reverse("index"), {'sort': 'desc'})
        self.assertEqual(response.status_code, 200)

        # Check if videos are displayed on the page
        self.assertContains(response, self.video1.name)
        self.assertContains(response, self.video2.name)
        self.assertContains(response, self.video3.name)

        # Check if videos are sorted correctly
        video_names = [self.video1.name, self.video2.name, self.video3.name]
        sorted_video_names = sorted(video_names, reverse=True)  # Sorting in descending order
        content = response.content.decode('utf-8')

        for i in range(2):
            video_index = content.index(sorted_video_names[i])
            next_video_index = content.index(sorted_video_names[i + 1])
            self.assertTrue(video_index < next_video_index)

    def test_search_index_view(self):
        """
        Test the search capabilities of the main page. 
        The video A and B match the searched word and should be displayed.
        The video C matches the searched word in caseless search and should be displayed.
        The video D does not contain the word Test and should not be displayed.
        """
        response = self.client.get(reverse("index"), {'search': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, VIDEO_NAME_A)
        self.assertContains(response, VIDEO_NAME_B)
        self.assertContains(response, VIDEO_NAME_C)
        self.assertNotContains(response, VIDEO_NAME_D)

    def test_detail_view(self):
        """
        Test the detail view of video the video A
        """
        response = self.client.get(reverse("detail", args=[self.video1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, VIDEO_NAME_A)
        self.assertContains(response, self.video1.iconUri)

    def test_nonexistent_detail_view(self):
        """
        Test that a detail view of nonexistant video returns 404
        """
        response = self.client.get(reverse("detail", args=[999]))
        self.assertEqual(response.status_code, 404)
        