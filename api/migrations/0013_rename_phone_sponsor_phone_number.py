# Generated by Django 5.1.6 on 2025-02-19 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_sponsor_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
