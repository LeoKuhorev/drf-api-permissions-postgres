from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'color',
                    'created_at', 'created_by')
    exclude = ('created_by', )
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
