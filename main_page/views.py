from django.shortcuts import render
from .models import Cars, CarsCategory

# Create your views here.
def main_page(request):
    categories = CarsCategory.objects.filter(is_visible=True)
    cars = Cars.objects.filter(is_visible=True)
    return render(request, 'main_page.html', context={
        'categories': categories,
        'cars': cars
    })
