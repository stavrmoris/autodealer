# Generated by Django 5.1.5 on 2025-02-09 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_car_final_price_remove_car_main_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Тип кузова')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Марка')),
            ],
        ),
        migrations.CreateModel(
            name='Drivetrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Привод')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, unique=True, verbose_name='Оценка')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='catalog.bodytype', verbose_name='Тип кузова'),
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='catalog.brand', verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='drivetrain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='catalog.drivetrain', verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='car',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='catalog.rating', verbose_name='Оценка'),
        ),
    ]
