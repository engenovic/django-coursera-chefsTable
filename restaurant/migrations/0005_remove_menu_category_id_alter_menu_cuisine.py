# Generated by Django 5.1.2 on 2024-10-27 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='category_id',
        ),
        migrations.AlterField(
            model_name='menu',
            name='cuisine',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='restaurant.menucategory'),
        ),
    ]
