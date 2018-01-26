from django.shortcuts import render
from django.http import HttpResponse
from django.conf import	settings

from rango.models import Category
from rango.models import Page

# Create your views here.

def index(request):
	category_list = Category.objects.order_by("-likes")[:5]
	pages_list = Page.objects.order_by("-views")[:5]
	context_dict = {"categories":category_list,"pages":pages_list}
	return render(request,'rango/index.html',context=context_dict)

def about(request):
	context_dict = {"MEDIA_URL":settings.MEDIA_URL}
	return render(request,'rango/about.html',context=context_dict)

def show_category(request,category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug="python")
		pages = Page.objects.filter(category = category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict["category"] = None
		context_dict["pages"] = None
	
	return render(request,'rango/category.html',context_dict)