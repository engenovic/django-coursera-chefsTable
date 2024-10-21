# Generated by Django 5.1.2 on 2024-10-21 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menucategory_menu_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='restaurant.menucategory'),
        ),
    ]
