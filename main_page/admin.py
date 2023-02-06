from django.contrib import admin
from .models import CarsCategory, Cars, AboutUs, Comments, UserReservation


# Register your models here.
class CarsInline(admin.TabularInline):
    model = Cars
    raw_id_fields = ['category']


admin.site.register(CarsCategory)
admin.site.register(Cars)
admin.site.register(AboutUs)
admin.site.register(Comments)
admin.site.register(UserReservation)
