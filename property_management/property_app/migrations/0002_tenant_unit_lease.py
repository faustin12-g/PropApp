# Generated by Django 5.0.2 on 2024-10-20 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.property')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rent_amount', models.IntegerField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.tenant')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property_app.unit')),
            ],
        ),
    ]
