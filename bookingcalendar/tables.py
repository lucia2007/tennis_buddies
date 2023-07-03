import django_tables2 as tables  # type: ignore


class BookingCalendarTable(tables.Table):
    """
    Creates a table with court availability
    """
    hour = tables.Column()
    one = tables.Column(verbose_name="Court One")
    two = tables.Column(verbose_name="Court Two")
    three = tables.Column(verbose_name="Court Three")
    four = tables.Column(verbose_name="Court Four")
    five = tables.Column(verbose_name="Court Five")

    class Meta:
        # model = BookingCalendar
        template_name = "django_tables2/bootstrap.html"
        # fields = ("court", )
