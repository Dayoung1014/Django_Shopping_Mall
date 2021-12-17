from django.contrib import admin
from .models import Item, Company, Category, Comment
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Item, MarkdownxModelAdmin)
admin.site.register(Company)
admin.site.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)