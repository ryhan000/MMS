from django.contrib import admin

from .models import Meal

class MealAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'pub_date')
    fieldsets = [
    (None, {'fields': ['name']}),
    (None, {'fields': ['meal_number']}),
    (None, {'fields': ['pub_date']}),
    ]
admin.site.disable_action('delete_selected')
admin.site.register(Meal, MealAdmin)

# Register your models here.
