"""
URL configuration for instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import HomeView, LoginView, ContactView, LegalView, RegisterView, logout_view, PerfilDetailView, PerfilUpdateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/<pk>/', PerfilDetailView.as_view(), name='profile_detail'),
    path('profile/update/<pk>/', PerfilUpdateView.as_view(), name='profile_update'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('legal/',LegalView.as_view(),name='legal'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
