from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}  # Automatically fills slug based on category_name
    list_display = ('category_name', 'slug')  # Displays these fields in the admin list view

admin.site.register(Category, CategoryAdmin)  # Registers the Category model with the custom admin class
