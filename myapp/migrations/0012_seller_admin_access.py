# Generated by Django 4.2.3 on 2023-08-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_display_image3_product_display_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='admin_access',
            field=models.BooleanField(default=False),
        ),
    ]