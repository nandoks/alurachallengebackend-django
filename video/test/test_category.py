from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from video.test.factories import CategoryFactory


class CategoryTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        category = CategoryFactory()
        category2 = CategoryFactory()


    def setUp(self):
        self.url = reverse('Categories-list')


    def test_get_request_for_listing_categories_total_should_be_2_and_return_200(self):
        """Tests if get request is working"""

        response = self.client.get(self.url)
        self.assertEquals(len(response.data), 2)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_request_creates_a_category_and_returns_201(self):
        """Tests if post request is working"""
        response = self.client.post(self.url, data={
            'title': 'test 123 12345',
            'color': '#123456',
        })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_put_request_updates_a_category_and_returns_200(self):
        """Tests if update request is working"""
        response = self.client.put("/categories/2/", data={
            'title': 'API',
            'color': '#987654',
        }, follow=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_request_returns_200_on_existing_category(self):
        """Tests if delete request is working"""
        response = self.client.delete("/categories/1/")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['detail'], 'Category successfuly deleted')

    def test_delete_request_returns_404_if_category_do_not_exists(self):
        """Tests if delete request is working"""
        response = self.client.delete("/categories/99/")
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.data['detail'], 'Category not found')


    def test_color_not_hex_color_must_return_400(self):
        """Tests if when creating a category color must be a hex value"""
        response = self.client.post(self.url, data={
            'title': 'test 123 12345',
            'color': '123456'
        })
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_color_accepts_hex_color_must_return_201(self):
        """Tests if creating a category with a hex valor for color is working"""
        response = self.client.post(self.url, data={
            'title': 'test 123 12345',
            'color': '#123456',
        })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_get_by_invalid_id_returns_error_message_and_404(self):
        """Tests if invalid id returns error message and 404"""
        response = self.client.get('/categories/99/')
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.data['detail'], 'Category not found')