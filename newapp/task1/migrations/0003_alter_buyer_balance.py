# Generated by Django 5.1.5 on 2025-01-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_buyer_balance_alter_game_age_limited_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
