from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    FILM = 'film'
    SOFTWARE = 'software'
    TYPE_CHOICES = [
        (FILM, 'Film'),
        (SOFTWARE, 'Software'),
    ]

    title= models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)
    roles = models.ManyToManyField(Role, related_name='projects', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    def __str__(self):
        return self.title

