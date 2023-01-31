from django.db import models
from django.core.validators import RegexValidator
import uuid
import os


# Create your models here.
class CarsCategory(models.Model):

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Cars(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/cars', filename)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(CarsCategory, on_delete=models.CASCADE)
    desc = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class AboutUs(models.Model):

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Comments(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/cars', filename)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name, blank=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class UserReservation(models.Model):

    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$', message='не вірний номер')
    email_validator = RegexValidator(regex=r'^[0-9A-Za-z](-?[0-9A-Za-z_])+@[0-9A-Za-z](-?[0-9A-Za-z._])+$',
                                     message='не вірний email')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    email_us = models.CharField(max_length=30, validators=[email_validator])
    date = models.DateField(auto_now_add=True)
    manager_data_processed = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', )

    def __str__(self):
        return f'{self.name} {self.phone} {self.email_us}'

