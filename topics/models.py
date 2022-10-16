from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.name


class New(models.Model):
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    source = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=400, null=True)
    value = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.text
