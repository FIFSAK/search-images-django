from django.db import models


class Request(models.Model):
    request = models.CharField("Request", max_length=50)

    def __str__(self):
        return self.request
