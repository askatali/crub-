from django.shortcuts import render
from django.views.generic import TemplateView
from asmovie.models import


class MovieView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        products = Movie.objects.all()
        return {'products': products}

