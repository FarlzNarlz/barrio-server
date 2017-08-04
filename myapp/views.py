from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
		return HttpResponse("Putas e o zé é paneleiro")
