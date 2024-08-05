from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from news.models import Publication, Category, PublicationComment, SocialNetwork, Address, ContactUs


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all()
        }
        return context

    def get(self, request, **kwargs):
        input_query = request.GET.get("query", "")
        print(input_query)
        find_publication = Publication.objects.filter(
            Q(title__icontains=input_query) |
            Q(title__iexact=input_query))
        context = {
            'publication_list': Publication.objects.all(),
            'publication_find': find_publication
        }
        return render(request, 'index.html', context)


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = {
            'social': SocialNetwork.objects.first(),
            'address': Address.objects.first()
        }
        return context

    def post(self, request):
        input_name = request.POST["name"]
        input_email = request.POST["email"]
        input_subject = request.POST["subject"]
        input_message = request.POST["message"]
        ContactUs.objects.create(name=input_name, email=input_email, subject=input_subject, message=input_message)
        context = {
            'social': SocialNetwork.objects.first(),
            'address': Address.objects.first()
        }
        return render(request, 'contact.html', context)


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
