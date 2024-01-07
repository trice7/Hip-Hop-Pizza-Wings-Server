# Generated by Django 4.1.3 on 2024-01-07 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=50)),
                ('is_admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField()),
                ('subtotal', models.IntegerField()),
                ('tip', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('total', models.IntegerField()),
                ('customer', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhpnwapi.paymenttype')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhpnwapi.employee')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhpnwapi.ordertype')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhpnwapi.foodtype')),
            ],
        ),
    ]
