from django.shortcuts import render
from django.http import HttpResponse
from django.conf import	settings

from rango.models import Category

# Create your views here.

def index(request):
	context_dict = {"boldmessage": "Crunchy,creamy,cookie,candy,cupcake!"}
	return render(request,'rango/index.html',context=context_dict)

def about(request):
	context_dict = {"MEDIA_URL":settings.MEDIA_URL}
	return render(request,'rango/about.html',context=context_dict)
