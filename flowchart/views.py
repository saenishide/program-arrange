from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .services import generate_flowchart
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_flowchart(request):
    generate_flowchart()
    return JsonResponse({"result": "ok"})