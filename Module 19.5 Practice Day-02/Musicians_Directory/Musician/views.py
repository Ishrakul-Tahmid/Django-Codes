from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView
# Create your views here.
from django.urls import reverse_lazy

class CreateMusicianView(CreateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('homepage')

class EditMusicianView(UpdateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')