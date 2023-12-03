from django.http import HttpResponse
from django.shortcuts import render


def show_afisha(request):
    return render(request, 'main.html')
