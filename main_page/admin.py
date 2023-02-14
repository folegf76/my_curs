from django.contrib import admin
from .models import CarsCategory, Cars, AboutUs, Comments, UserReservation

@admin.register(CarsCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'price', 'desc']
    list_filter = ['is_visible', 'price', 'position']
    list_editable = ['price', 'is_visible']


@admin.register(Cars)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'photo', 'desc', 'category']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible']


@admin.register(UserReservation)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email_us', 'date', 'manager_data_processed', 'is_processed']
    list_filter = ['is_processed', 'phone', 'manager_data_processed']
    list_editable = ['is_processed']


@admin.register(AboutUs)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'desc']
    list_filter = ['is_visible', 'name']
    list_editable = ['is_visible']


@admin.register(Comments)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'desc', 'photo']
    list_filter = ['is_visible', 'name']
    list_editable = ['is_visible']


