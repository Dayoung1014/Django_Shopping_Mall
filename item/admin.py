from django.contrib import admin
from .models import Item, Company, Category
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Item, MarkdownxModelAdmin)
admin.site.register(Company)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)