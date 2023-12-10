from django.contrib import admin
from .models import ToDo
from .models import Profile

admin.site.register(ToDo)


admin.site.register(Profile)