# Generated by Django 5.0.1 on 2024-05-07 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_beauty', '0003_customer_appointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]