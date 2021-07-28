import factory

from video.models import Category, Video


class CategoryFactory(factory.Factory):
    class Meta:
        model = Category
        django_get_or_create = ('title','color')

    title = 'LIVRE'
    color = '#959595'


class VideoFactory(factory.Factory):
    class Meta:
        model = Video
        django_get_or_create = ('title','description','url')

    title = factory.Faker('name')
    description = factory.Faker('text')
    url = 'http://alura.com.br'