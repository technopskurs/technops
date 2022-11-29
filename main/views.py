from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
def index(request):
    return render(request, 'main/index.html')

class LoginUser(LoginView):
    form_class = LoginUserForms
    template_name = 'registration/login.html'

class Register(CreateView):
    form_class = RegisterUserForms
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)