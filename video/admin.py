from django.contrib import admin

# Register your models here.
from video.models import Video


class Videos(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao', 'url']
    list_display_links = ['id', 'titulo']
    list_per_page = 15


admin.site.register(Video, Videos)
