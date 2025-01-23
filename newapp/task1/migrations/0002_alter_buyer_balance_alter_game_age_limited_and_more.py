# Generated by Django 5.1.5 on 2025-01-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='age_limited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
