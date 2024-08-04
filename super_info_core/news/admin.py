from django.contrib import admin

from news.models import Publication, PublicationComment, Hashtag, Category


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']
