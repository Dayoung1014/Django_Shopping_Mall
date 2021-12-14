from django.contrib import admin
from .models import Item, Company, Category

# Register your models here.
admin.site.register(Item)
admin.site.register(Company)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)