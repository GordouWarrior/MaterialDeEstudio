from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import MaterialDeEstudio


class HomePageView(ListView):
    model = MaterialDeEstudio
    template_name = 'home.html'

