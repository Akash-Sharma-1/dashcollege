from django.shortcuts import render
from django.views import generic


class Pool(generic.TemplateView):
    template_name = "pool.html"


class PoolResource(generic.TemplateView):
    template_name = "pool.html"
