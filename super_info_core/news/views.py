from django.shortcuts import render
from django.views.generic import TemplateView

from news.models import Publication, Category


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all()
        }
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']

        context = {
            'publication': Publication.objects.get(id=publication_pk),
            'categories': Category.objects.all()
        }
        return context
