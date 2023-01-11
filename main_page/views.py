from django.shortcuts import render
from .models import Cars, CarsCategory

# Create your views here.
def main_page(request):
    categories = CarsCategory.objects.filter(is_visible=True)
    car = Cars.objects.filter(is_visible=True)
    return render(request, 'index.html')
