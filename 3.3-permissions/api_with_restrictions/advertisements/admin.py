from django.contrib import admin


class AdvertisementAdmin(admin.ModelAdmin):
	list_display = 'id', 'title', 'creator', 'created_at', 'updated_at', 'status',
