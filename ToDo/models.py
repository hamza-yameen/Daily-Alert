from django.db import models


class Todo_app(models.Model):
    addDate = models.DateTimeField()
    text = models.CharField(max_length=200)
