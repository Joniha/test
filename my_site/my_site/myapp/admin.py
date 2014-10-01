from django.contrib import admin
from django.db.models import get_model
from my_site.myapp.models import list_names

for key in list_names:
	model = get_model('myapp', key)
	admin.site.register(model)
