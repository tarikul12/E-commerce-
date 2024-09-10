from django.db import models

class Intent(models.Model):
    name = models.CharField(max_length=255)
    keywords = models.TextField()

class Entities(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)

class UserMessage(models.Model):
    message = models.TextField()
    intent = models.ForeignKey(Intent, on_delete=models.SET_NULL, null=True)
    entities = models.ManyToManyField(Entities, blank=True)