from django.contrib import admin
from .models import Category, Product, Contact, About

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'created', 'updated']
    prepopulated_fields = {'slug':('title',)}
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','phone','message']

@admin.register(About)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'about']
