# Generated by Django 5.0.7 on 2024-08-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_rename_cara_value_carinventory_cars_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
