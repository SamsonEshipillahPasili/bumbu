from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
