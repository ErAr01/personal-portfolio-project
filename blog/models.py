from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.title

