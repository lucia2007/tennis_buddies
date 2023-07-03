from django.contrib import admin  # type: ignore
from .models import Booking, Event, Court
# from buddies.models import UserProfile  # type: ignore


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

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


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'date', 'time', 'court']
    list_filter = ['event_type', ]
    search_fields = ['start_time', 'event_type']


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
    search_fields = ['name', ]
