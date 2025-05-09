# Generated by Django 5.2 on 2025-04-27 16:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productpricehistory_change_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_strategy_change',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='pricing_strategy',
            field=models.CharField(choices=[('RL', 'Reinforcement Learning'), ('STATIC', 'Traditional Static Pricing')], default='RL', max_length=10),
        ),
    ]
