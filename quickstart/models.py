from django.db import models

# Create your models here.


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True,
                            default='dori', unique=True)
    objects = models.Manager()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
