from rest_framework.test import APITestCase
from video.models import Video
from django.urls import reverse
from rest_framework import status


class VideoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Videos-list')
        self.video_1 = Video.objects.create(
            titulo="Boas práticas no Django 3: apps, pastas e paginação",
            descricao="Paginação com Django",
            url="https://cursos.alura.com.br/course/django-2-boas-praticas"
        )
        self.video_2 = Video.objects.create(
            titulo="API com Django 3: Aprofundando em testes e documentação",
            descricao="API test com django",
            url="https://cursos.alura.com.br/course/api-django-3-testes-documentacao"
        )
        self.video_3 = Video.objects.create(
            titulo="API com Django 3: Aprofundando em testes e documentação",
            descricao="API test com django",
            url="https://cursos.alura.com.br/course/api-django-3-testes-documentacao"
        )

    def test_put_request_for_updating_a_video(self):
        """Test if UPDATE resquest is updating a video"""

        response = self.client.put('/videos/1/', data={
            'titulo': 'Boas práticas no Django 3: apps, pastas e paginação',
            'descricao': 'Paginação com Django atualizado',
            'url': 'https://cursos.alura.com.br/course/django-2-boas-praticas'
        })
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_request_for_listing_videos(self):
        """Test if GET request is returning a list of videos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_request_for_creating_a_video(self):
        """Test if POST request is creating a video"""
        data = {
            'titulo': 'API com Django 3: Versionamento, cabeçalhos e CORS',
            'descricao': 'API com django 3, aprofundando o conhecimento',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.list_url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_request_for_deleting_a_video(self):
        """Test if DELETE resquest is updating a video"""
        response = self.client.delete('/videos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
