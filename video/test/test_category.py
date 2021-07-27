from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase

from video.models import Video, Category


class CategoryTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('Categories-list')
        Category.objects.create(
            title='Programação',
            color='#123546',
        )
        Category.objects.create(
            title='DevOps',
            color='#987654',
        )

    def tearDown(self):
        pass

    def test_get_request_for_listing_categories_total_should_be_2(self):
        response = self.client.get(self.url)
        self.assertEquals(len(response.data), 2)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_request_creates_a_category(self):
        response = self.client.post(self.url, data={
            'title': 'test 123 12345',
            'color': '#123456',
        })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_put_request_updates_a_video(self):
        response = self.client.put("/categories/" + str(Category.objects.last().id), data={
            'title': 'API',
            'color': '#987654',
        }, follow=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_request_delete_a_video(self):
        response = self.client.delete("/categories/" + str(Category.objects.last().id), follow=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


    def test_color_not_hex_color_must_return_400(self):
        response = self.client.post(self.url, data={
            'title': 'test 123 12345',
            'color': '123456'
        })
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_color_accepts_hex_color_must_return_201(self):
        response = self.client.post(self.url, data={
            'title': 'test 123 12345',
            'color': '#123456',
        })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
