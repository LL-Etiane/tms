# Generated by Django 3.2.4 on 2021-11-30 03:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_matricule'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='date_creaetd',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]