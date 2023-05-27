from django.shortcuts import render
from arbeitsplanung.models import Arbeitsplan
from django.urls import reverse

def home(request):
    return render(request, 'home.html')


