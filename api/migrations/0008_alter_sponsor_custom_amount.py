# Generated by Django 5.1.6 on 2025-02-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_sponsor_spent_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='custom_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
    ]
