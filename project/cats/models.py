# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Cat(models.Model):
    """Feline catus."""

    name = models.CharField(
            max_length=50,
            unique=True,
            )

    nickname = models.CharField(
            max_length=50,
            blank=True,
            )

    age = models.IntegerField(
            null = True,
            blank = True,
            )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat_detail', pk=self.id)


