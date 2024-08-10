from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import telebot
from config import API_TOKEN_BOT
from news.models import Publication, Category, PublicationComment, SocialNetwork, Address, ContactUs

bot = telebot.TeleBot(API_TOKEN_BOT)
LOID = 7065054223


class HomeView(ListView):
    model = Publication
    template_name = 'index.html'

    def get(self, request, **kwargs):
        input_query = request.GET.get("query", "")
        print(input_query)

        category_pk = request.GET.get("category_pk", "")
        if category_pk:
            publications = Publication.objects.filter(category_id=category_pk, is_active=True)
        else:
            publications = Publication.objects.filter(is_active=True)
        find_publication = Publication.objects.filter(
            Q(title__icontains=input_query) |
            Q(title__iexact=input_query))
        context = {
            'publication_list': publications,
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
        bot.send_message(LOID, F"Новое сообщение от пользователя:\n Имя: {input_name},\n email: {input_email}, \n\n {input_subject}, \n\n {input_message}")
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
        bot.send_message(LOID, F"К вашему публикацию {publication.title} написали комментарий\n имя: {input_name}\n Комменатарий: {input_text}")
        return render(request, "publication-detail.html", context=context)
