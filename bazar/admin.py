from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Item, Bazar


class ItemInline(admin.StackedInline):
    model = Item
    extra = 3


class BazarAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'pub_date',)
    inlines = [ItemInline]


admin.site.site_header = 'MMS Admin Dashboard'
admin.site.unregister(Group)
admin.site.register(Bazar, BazarAdmin)
