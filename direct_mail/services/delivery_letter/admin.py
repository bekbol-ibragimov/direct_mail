from django.contrib import admin

from .models import DeliveryType,Letter


@admin .register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_created']
    list_filter = ['customer']

