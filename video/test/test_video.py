from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from video.models import Video, Category
from video.test.factories import VideoFactory, CategoryFactory


class VideoTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        category = CategoryFactory()
        video = VideoFactory()
        video2 = VideoFactory()
        video3 = VideoFactory()
        category.save()
        video.save()
        video2.save()
        video3.save()

    def setUp(self):
        self.url = reverse('Videos-list')


    # def tearDown(self):
    #     self.category.delete()
    #     self.video.delete()
    #     self.video2.delete()
    #     self.video3.delete()


    def test_title_cannot_have_less_than_5_characters(self):
        """Test if title cannot have less than 5 characters"""
        data = {
            'title': 'four',
            'description': 'API com django 3, aprofundando o conhecimento',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.url, data=data)
        self.assertLess(len(data['title']), 5)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(Video.objects.count(), 3)

    def test_title_must_have_at_least_5_characters(self):
        """Test if title must have at least 5 characters"""
        data = {
            'title': 'seven',
            'description': 'API com django 3, aprofundando o conhecimento',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.url, data=data)
        self.assertGreaterEqual(len(data['title']), 5)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Video.objects.count(), 4)

    def test_description_cannot_have_less_than_10_characters(self):
        """Test if description cannot have less than 5 characters"""
        data = {
            'title': 'API com Django 3: Versionamento, cabeçalhos e CORS',
            'description': 'five+',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.url, data=data)
        self.assertLess(len(data['description']), 10)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(Video.objects.count(), 3)

    def test_description_must_have_at_least_10_characters(self):
        """Test if description must have at least 10 characters"""
        data = {
            'title': 'API com Django 3: Versionamento, cabeçalhos e CORS',
            'description': 'ten letters',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.url, data=data)
        self.assertGreaterEqual(len(data['description']), 10)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Video.objects.count(), 4)

    def test_url_must_have_dot_something_and_http(self):
        """Test if url is a valid URL with http:// and .something"""
        data = {
            'title': 'API com Django 3: Versionamento, cabeçalhos e CORS',
            'description': 'ten letters',
            'url': 'NoHttpAndNoDotSomething'
        }
        response = self.client.post(self.url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data['url'] = 'http://NoHttpAndNoDotSomething'
        response = self.client.post(self.url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data['url'] = 'NoHttpAndNoDotSomething.com'
        response = self.client.post(self.url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data['url'] = 'http://NoHttpAndNoDotSomething.com'
        response = self.client.post(self.url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_video_must_have_a_category(self):
        """Test if creating a video adds category 1 if no category is passed"""
        data = {
            'title': 'API com Django 3: Versionamento, cabeçalhos e CORS',
            'description': 'API com django 3, aprofundando o conhecimento',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.url, data)
        video = Video.objects.last()
        self.assertEquals(video.category.id, 1)
        self.assertEquals(video.category.title, 'LIVRE')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Video.objects.count(), 4)

    def test_put_request_for_updating_a_video(self):
        """Test if UPDATE resquest is updating a video"""
        response = self.client.put(f'/videos/1/', data={
            'title': 'Boas práticas no Django 3: apps, pastas e paginação',
            'description': 'Paginação com Django atualizado',
            'url': 'https://cursos.alura.com.br/course/django-2-boas-praticas'
        }, follow=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_request_for_listing_videos_total_should_be_3(self):
        """Test if GET request is returning a list of videos"""
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Video.objects.count(), 3)

    def test_post_request_for_creating_a_video_total_should_be_4(self):
        """Test if POST request is creating a video"""
        data = {
            'title': 'API com Django 3: Versionamento, cabeçalhos e CORS',
            'description': 'API com django 3, aprofundando o conhecimento',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Video.objects.count(), 4)

    def test_delete_request_for_deleting_a_video_total_should_be_2(self):
        """Test if DELETE resquest is deleting a video"""
        response = self.client.delete('/videos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Video.objects.count(), 2)