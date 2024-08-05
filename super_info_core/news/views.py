from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from news.models import Publication, Category, PublicationComment


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

    def post(self, request, **kwargs):
        publication_pk = kwargs['pk']
        input_name = request.POST["name"]
        input_text = request.POST["message"]
        publication = Publication.objects.get(id=publication_pk)
        context = {
            'publication': Publication.objects.get(id=publication_pk),
            'categories': Category.objects.all()
        }
        PublicationComment.objects.create(name=input_name, text=input_text, publication=publication)
        return render(request, "publication-detail.html", context=context)
