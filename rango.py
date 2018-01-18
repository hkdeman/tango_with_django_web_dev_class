import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
						'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
	python_pages = [
		{"title":"Official Python Tutorial",
		  "url":"https://docs.python.org/2/tutorial/"},
		  {"title":"How to Think like a Computer Scientist",
		   "url":"https://www.greenteapress.com/thinkpython/"}
	]