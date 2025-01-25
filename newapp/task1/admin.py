from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('size', 'cost')
    list_display = ('title', 'cost', 'size', )
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age', )
    list_display = ('name', 'balance', 'age', )
    search_fields = ('name', )
    list_per_page = 30
    readonly_fields = ('balance', )

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ('title', 'content')
    list_display = ('title', 'content', 'date')
