from django.contrib import admin
from django.contrib.admin import ModelAdmin

from firstapp.models import Dishes


@admin.register(Dishes)
class DishesAdmin(ModelAdmin):
    pass
