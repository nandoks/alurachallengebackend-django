from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from video.models import Video


class VideoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Videos-list')
        self.video_1 = Video(
            title="Boas práticas no Django 3: apps, pastas e paginação",
            description="Paginação com Django",
            url="https://cursos.alura.com.br/course/django-2-boas-praticas"
        )
        self.video_2 = Video(
            title="API com Django 3: Aprofundando em testes e documentação",
            description="API test com django",
            url="https://cursos.alura.com.br/course/api-django-3-testes-documentacao"
        )
        self.video_3 = Video(
            title="API com Django 3: Aprofundando em testes e documentação",
            description="API test com django",
            url="https://cursos.alura.com.br/course/api-django-3-testes-documentacao"
        )
        self.video_1.save()
        self.video_2.save()
        self.video_3.save()

    def tearDown(self):
        self.video_1.delete()
        self.video_2.delete()
        self.video_3.delete()

    def test_put_request_for_updating_a_video(self):
        """Test if UPDATE resquest is updating a video"""
        response = self.client.put(f'/videos/{self.video_1.id}', data={
            'title': 'Boas práticas no Django 3: apps, pastas e paginação',
            'description': 'Paginação com Django atualizado',
            'url': 'https://cursos.alura.com.br/course/django-2-boas-praticas'
        }, follow=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_request_for_listing_videos_total_should_be_3(self):
        """Test if GET request is returning a list of videos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Video.objects.count(), 3)

    def test_post_request_for_creating_a_video_total_should_be_4(self):
        """Test if POST request is creating a video"""
        data = {
            'title': 'API com Django 3: Versionamento, cabeçalhos e CORS',
            'description': 'API com django 3, aprofundando o conhecimento',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.list_url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Video.objects.count(), 4)

    def test_delete_request_for_deleting_a_video_total_should_be_2(self):
        """Test if DELETE resquest is updating a video"""
        response = self.client.delete('/videos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Video.objects.count(), 2)
