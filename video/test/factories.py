import factory

from video.models import Category, Video


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = 'LIVRE'
    color = '#959595'


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Video

    title = factory.Faker('name')
    description = factory.Faker('text')
    url = 'http://alura.com.br'