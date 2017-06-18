# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

from models import Cat
from forms import TweetForm

class CatListView(generic.ListView):
    model = Cat


class CatDetailView(generic.DetailView):
    model = Cat


class CatCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Cat
    permission_required = "cats.can_add"
    fields = ['name', 'age', 'nickname']


class CatUpdateView(generic.UpdateView):
    model = Cat
    fields = ['name', 'age', 'nickname']


class TweetView(generic.FormView):
    form_class = TweetForm
    template_name = "cats/tweet_form.html"
    success_url = "/cats/"
    
