from django.contrib import admin
from phones.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'price', 'image', 'lte_exists', 'release_date', 'slug']
