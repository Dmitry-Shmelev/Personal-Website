import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

# Create your models here.


class UserInfo(models.Model):
    first_name = models.CharField(max_length=20, default="Dmitry")
    last_name = models.CharField(max_length=20, default="Shmelev")

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class LatestProject(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='projects')
    description = models.TextField(blank=True)
    pub_date = models.DateField(blank=True)
    project_URL = models.URLField(blank=True)

    def image_preview(self):
        return mark_safe('<img src="{url}" width="160" height="120" ><image/>'.format(
            url=self.image.url,
        ))
    image_preview.allow_tags = True

    def __str__(self):
        return self.title
