from django.contrib import admin
from .models import *

class RevExpAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Car)
admin.site.register(Expense)
admin.site.register(Revenue,RevExpAdmin)
admin.site.register(CarDocument)
