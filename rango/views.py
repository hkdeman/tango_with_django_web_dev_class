from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	string = "Rango says here is the home page"
	link = "<a href='/rango/about/'>About</a>"
	return HttpResponse(string+"\n"+link)

def about(request):
	string = "Rango says here is the about page"
	link = "<a href='/rango/'>Home</a>"
	return HttpResponse(string+"\n"+link)
