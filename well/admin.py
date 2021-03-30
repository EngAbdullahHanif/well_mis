from django.contrib import admin

# Register your models here.
from .models import Well, Monitor

admin.site.register(Well)
admin.site.register(Monitor)