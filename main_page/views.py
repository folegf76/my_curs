from django.shortcuts import render
from .models import Cars, CarsCategory, AboutUs, Comments

# Create your views here.
def main_page(request):
    categories = CarsCategory.objects.filter(is_visible=True)
    cars = Cars.objects.filter(is_visible=True)
    about_us = AboutUs.objects.filter(is_visible=True)
    comments = Comments.objects.filter(is_visible=True)

    return render(request, 'main_page.html', context={
        'categories': categories,
        'cars': cars,
        'about_us': about_us,
        'comments': comments
    })
