from django.contrib import admin
from .models import Person, ModelX

# Register your models here.
admin.site.register({Person,ModelX})
#admin.site.register(ModelX)
