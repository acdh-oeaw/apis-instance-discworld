from django.db import models
from apis_core.apis_entities.models import AbstractEntity


class Character(AbstractEntity):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Place(AbstractEntity):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Book(AbstractEntity):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
