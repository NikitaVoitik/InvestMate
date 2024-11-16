from django.contrib import admin
from .models import Asset, PriceHistory


# Register your models here.

@admin.register(Asset)
class MyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceHistory)
class MyModelAdmin(admin.ModelAdmin):
    pass
