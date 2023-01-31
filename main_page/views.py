from django.shortcuts import render, redirect
from .models import Cars, CarsCategory, AboutUs, Comments
from .forms import UserReservationForm


# Create your views here.
def main_page(request):
    if request.method == 'POST':
        form_reserve = UserReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    categories = CarsCategory.objects.filter(is_visible=True)
    cars = Cars.objects.filter(is_visible=True)
    about_us = AboutUs.objects.filter(is_visible=True)
    comments = Comments.objects.filter(is_visible=True)
    form_reserve = UserReservationForm()

    return render(request, 'main_page.html', context={
        'categories': categories,
        'cars': cars,
        'about_us': about_us,
        'comments': comments,
        'form_reserve': form_reserve,
    })
