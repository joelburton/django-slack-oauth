# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Cat

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """Admin view for cats."""

    fields = ['name', 'age']

