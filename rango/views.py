from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	context_dict = {"boldmessage": "Crunchy,creamy,cookie,candy,cupcake!"}
	return render(request,'rango/index.html',context=context_dict)

def about(request):
	string = "Rango says here is the about page"
	link = "<a href='/rango/'>Home</a>"
	return HttpResponse(string+"\n"+link)
