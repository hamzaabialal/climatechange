from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'


class ElementsPageView(TemplateView):
    template_name = 'elements.html'


class GenericPageView(TemplateView):
    template_name = 'generic.html'