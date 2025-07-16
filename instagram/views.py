from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from django.contrib.auth.models import User

class HomeView(TemplateView):
    template_name = "general/home.html"


class LoginView(TemplateView):
    template_name = "general/login.html"
    

class RegisterView(CreateView):
    template_name = "general/register.html"
    model = User
    success_url = reverse_lazy('home')
    form_class = RegistrationForm
    
class RegisterView(TemplateView):
    template_name = "general/register.html"
    
class LegalView(TemplateView):
    template_name = "general/register.html"
    

class ContactView(TemplateView):
    template_name = "general/contact.html"