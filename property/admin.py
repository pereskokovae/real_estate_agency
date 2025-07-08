from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = [
        '__str__',
        'new_building',
        'construction_year',
        'owner_pure_phone',
        'owners_phonenumber'
        ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['apartments']


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
