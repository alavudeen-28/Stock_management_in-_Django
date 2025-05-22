 # Import the Stock model
from django.contrib import admin
from .models import *
from .forms import StockCreateForm  # Import the form

class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']

admin.site.register(Stock, StockCreateAdmin)  # ✅ Correct
admin.site.register(Category)
