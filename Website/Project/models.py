from django.db import models
import uuid
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # owner=
    featured_image = models.ImageField(
        null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created_field = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        img = ''
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_field = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Certifications(models.Model):
    name = models.CharField(max_length=350)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
