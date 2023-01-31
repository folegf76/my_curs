from django import forms
from .models import UserReservation


class UserReservationForm(forms.ModelForm):

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                           'type': "text",
                           'placeholder': "Ваше Імя:"}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
                           'type': "tel",
                           'placeholder': "Ваш номер телефона:"}))
    email_us = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
                           'type': "email",
                           'placeholder': "Ваш Email:"}))

    class Meta:
        model = UserReservation
        fields = ('name', 'phone', 'email_us')