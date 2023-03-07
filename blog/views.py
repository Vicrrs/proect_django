from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# index -> primeiro arquivo chamado quando executado
def index(request):
    return HttpResponse("Olá mundo")
