from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PublicationComment(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()


class Publication(models.Model):
    is_new = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=300)
    description = RichTextField()
    image = models.ImageField(null=True)
    created_at = models.DateField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag, null=True, related_name='publications')
