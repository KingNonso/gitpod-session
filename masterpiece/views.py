from django.shortcuts import render
from django.views import generic

from masterpiece.forms import ContactForm
from masterpiece.models import Contact


class CreateContactView(generic.CreateView):
    template_name = 'masterpiece/index.html'
    success_url = '/'
    form_class = ContactForm


def standard_python():
    return 2 + 2


