from statistics import mode
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64)
    contents = models.TextField()
    writer = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    board_name = models.CharField(max_length=64)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)