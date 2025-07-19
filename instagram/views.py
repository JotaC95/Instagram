from django.views.generic import TemplateView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm, loginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from profiles.models import UserProfile as Profile


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
    template_name = "general/legal.html"
    

class ContactView(TemplateView):
    template_name = "general/contact.html"
    
class PerfilDetailView(DetailView):
    model = Profile
    template_name = "general/profile_detail.html"
    context_object_name = 'profile'
    
class PerfilUpdateView(UpdateView):
    model = Profile
    template_name = "general/profile_update.html"
    context_object_name = 'profile'
    fields = ['profile_picture', 'bio', 'birth_date']
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Perfil actualizado exitosamente")
        return super(PerfilUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('profile_detail', args=[self.object.pk])
    

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesión exitosamente")
    return HttpResponseRedirect(reverse('home'))