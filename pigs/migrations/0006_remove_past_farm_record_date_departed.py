# Generated by Django 5.1.2 on 2024-11-02 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pigs', '0005_alter_immunization_pig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='past_farm_record',
            name='date_departed',
        ),
    ]
