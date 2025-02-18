from django.contrib import admin
from .models import Order, Item

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total',)
    inlines = [ItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
