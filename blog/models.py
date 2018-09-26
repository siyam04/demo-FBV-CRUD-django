from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    author = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
