from django.db import models

class weather(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class meta:
        verbose_name_plural = 'cities'