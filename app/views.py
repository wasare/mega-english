from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Mega English - Sua primeira opção de aprender inglês.")

