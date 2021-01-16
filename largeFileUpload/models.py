from django.db import models
from django.urls import reverse


class File(models.Model):
    file = models.FileField()

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return reverse('largeFileUpload:index')
