from django.contrib import admin
from .models import Shows

# Register your models here.

class ShowsAdmin(admin.ModelAdmin):
    shows_display = (
        'name',
        'start_date',
        'end_date',
        'theatre',
        'on_sale',
        'in_future',
    )

    ordering = ('name',)


admin.site.register(Shows, ShowsAdmin)
