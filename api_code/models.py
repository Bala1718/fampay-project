from django.db import models
from django.shortcuts import render


class Youtubevideo(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    unique_id = models.CharField(max_length=100)
    published_at = models.CharField(max_length=1000)

    class Meta:
        app_label = 'api_code.models.Youtubevideo'


