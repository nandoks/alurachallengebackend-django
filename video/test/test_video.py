from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from video.models import Video, Category


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

    def test_title_cannot_have_less_than_5_characters(self):
        """Test if title cannot have less than 5 characters"""
        data = {
            'title': 'four',
            'description': 'API com django 3, aprofundando o conhecimento',
            'url': 'https://cursos.alura.com.br/course/api-django-3-versionamento-cabecalhos-cors'
        }
        response = self.client.post(self.list_url, data=data)
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
        response = self.client.post(self.list_url, data=data)
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

        response = self.client.post(self.list_url, data=data)
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
        response = self.client.post(self.list_url, data=data)
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
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data['url'] = 'http://NoHttpAndNoDotSomething'
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data['url'] = 'NoHttpAndNoDotSomething.com'
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data['url'] = 'http://NoHttpAndNoDotSomething.com'
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
