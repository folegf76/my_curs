from django.contrib import admin
from .models import CarsCategory, Cars, AboutUs, Comments

# Register your models here.
admin.site.register(CarsCategory)
admin.site.register(Cars)
admin.site.register(AboutUs)
admin.site.register(Comments)
