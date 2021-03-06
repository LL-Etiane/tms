# Generated by Django 3.2.4 on 2021-11-22 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='car',
            field=models.ManyToManyField(to='cars.Car'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='shift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.shift'),
        ),
    ]
