# Generated by Django 4.1.5 on 2023-01-12 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_aboutus_comments_alter_cars_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='не вірний номер', regex='^\\+?3?8?0\\d{2}[- ]?(\\d[- ]?){7}$')])),
                ('email_us', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='не вірний email', regex='^[0-9A-Za-z](-?[0-9A-Za-z_])+@[0-9A-Za-z](-?[0-9A-Za-z._])+$')])),
                ('date', models.DateField(auto_now_add=True)),
                ('manager_data_processed', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]