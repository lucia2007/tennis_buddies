from django.contrib import admin  # type: ignore
from .models import Booking, Court


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Display Booking details in Admin panel
    """
    list_display = (
                    'pk',
                    'owner',
                    'get_opponents',
                    'date',
                    'time',
                    'court',
                    'email_sent'
                    )

    @admin.display(
        ordering='user_profile__first_name', description='Opponents'
        )
    def get_opponents(self, obj):
        # makes a string of all chosen opponents
        return ', '.join(sorted(map(str, obj.opponents.all())))

    search_fields = ['user_profile', 'court', 'opponents']
    list_filter = ['court', ]


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
    search_fields = ['name', ]
