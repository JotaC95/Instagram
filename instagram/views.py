from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm, loginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView

class HomeView(TemplateView):
    template_name = "general/home.html"


class LoginView(FormView):
    template_name = "general/login.html"
    form_class = loginForm
    
    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.add_message(
                self.request, messages.SUCCESS, f"Bienvenido de nuevo {user.username}!")
            return HttpResponseRedirect(reverse('home'))
        
        else:
            messages.add_message(
                self.request, messages.ERROR, "Usuario o contraseña incorrectos")
        return super(LoginView, self).form_invalid(form)
    

class RegisterView(CreateView):
    template_name = "general/register.html"
    model = User
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    
    def form_valid(self, form):
        messages.add_message(self.request,messages.SUCCESS, "Usuario creado exitosamente")
        return super(RegisterView, self).form_valid(form)
    
class LegalView(TemplateView):
    template_name = "general/register.html"
    

class ContactView(TemplateView):
    template_name = "general/contact.html"