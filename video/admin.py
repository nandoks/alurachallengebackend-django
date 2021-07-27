from django.contrib import admin

# Register your models here.
from video.models import Video, Category


class Videos(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'url', ]
    list_display_links = ['id', 'title', ]
    list_per_page = 15


admin.site.register(Video, Videos)


class Categories(admin.ModelAdmin):
    list_display = ['id', 'title', 'color']
    list_display_links = ['id', 'title']
    list_per_page = 15


admin.site.register(Category, Categories)
