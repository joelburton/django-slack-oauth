# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from cats.models import Cat

class CatModelTest(TestCase):
    def test_can_add(self):
        auden = Cat(name='Auden')
        auden.save()
        auden = Cat.objects.first()
        self.assertEqual(auden.name, "Auden")


class CatViewsTest(TestCase):
    def setUp(self):
        auden = Cat(name='Auden')
        auden.save()
    def test_can_view(self):
        response = self.client.get("/cats/1/")
        self.assertContains(response, "Auden")
    def test_can_update(self):
        response = self.client.get("/cats/1/-edit/")
        self.assertContains(response, "Edit Cat")


