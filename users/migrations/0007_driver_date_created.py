# Generated by Django 3.2.10 on 2021-12-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_driver_nic'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='date_created',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]