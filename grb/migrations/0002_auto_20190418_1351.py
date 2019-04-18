# Generated by Django 2.1.7 on 2019-04-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='booking_status',
            field=models.CharField(choices=[('B', 'Booked'), ('P', 'Pending'), ('C', 'Cancelled')], default='P', max_length=1),
        ),
    ]