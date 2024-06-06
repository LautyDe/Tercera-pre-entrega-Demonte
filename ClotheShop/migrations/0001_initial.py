# Generated by Django 5.0.6 on 2024-06-06 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
            ],
            options={
                'ordering': ('model', 'size'),
            },
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
            ],
            options={
                'ordering': ('model', 'size'),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('shirts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClotheShop.shirt')),
                ('shoes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClotheShop.shoe')),
            ],
        ),
    ]