from django.shortcuts import render
from django.http import HttpResponse
from .services import generate_flowchart

def index(request):
    generate_flowchart()
    return HttpResponse("Hello, world. You're at the flowchart index.")