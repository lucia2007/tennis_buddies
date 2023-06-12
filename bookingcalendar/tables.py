import django_tables2 as tables


class BookingCalendarTable(tables.Table):
    hour = tables.Column()
    one = tables.Column()
    two = tables.Column()
    three = tables.Column()
    four = tables.Column()
    five = tables.Column()

    class Meta:
        # model = BookingCalendar
        template_name = "django_tables2/bootstrap.html"
        # fields = ("court", )
