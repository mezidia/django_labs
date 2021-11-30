from django.contrib import admin
from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_filter = ('id',)
    search_fields = ['destination_from', 'destination_to']
