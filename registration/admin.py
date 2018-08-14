from django.contrib import admin

# Register your models here.
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('name', 'regi_date')
	fieldsets = [
     (None, {'fields': ['name']}),
     (None, {'fields': ['phn']}),
     (None, {'fields': ['regi_date']}),
	]
admin.site.register(Registration, RegistrationAdmin)