from django.contrib import admin
from .models import CarsCategory, Cars, AboutUs, Comments, UserReservation

# Register your models here.
admin.site.register(CarsCategory)
admin.site.register(Cars)
admin.site.register(AboutUs)
admin.site.register(Comments)
admin.site.register(UserReservation)
