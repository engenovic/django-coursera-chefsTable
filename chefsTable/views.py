from django.http import HttpResponse
from django.shortcuts import render


def handler404(request, exception):
    return HttpResponse("404: Page not Found")