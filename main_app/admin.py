from django.contrib import admin
from .models import Beer, LikeBeerUser, Restaurant

# Register your models here.
admin.site.register(Beer)
admin.site.register(LikeBeerUser)
admin.site.register(Restaurant)
