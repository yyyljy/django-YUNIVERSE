from statistics import mode
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64)
    contents = models.TextField()
    writer = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    board_name = models.CharField(max_length=64, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0, blank=True)

    @property
    def update_hits(self):
        self.hits = self.hits + 1
        self.save()

    def __str__(self):
        return f'{self.id}번째글 - {self.title} : {self.contents}'

