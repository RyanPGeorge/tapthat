from django.contrib import admin
from .models import Beer, LikeBeerUser

# Register your models here.
admin.site.register(Beer)
admin.site.register(LikeBeerUser)

