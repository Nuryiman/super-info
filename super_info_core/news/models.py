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


class Publication(models.Model):
    is_new = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='publications')
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=300)
    description = RichTextField()
    image = models.ImageField(null=True)
    created_at = models.DateField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag, null=True, related_name='publications')

    def __str__(self):
        return self.title


class PublicationComment(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, related_name='comments')


class Address(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    last_text = models.CharField(max_length=100)


class SocialNetwork(models.Model):
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
