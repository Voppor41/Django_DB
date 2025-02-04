# Generated by Django 5.1.5 on 2025-01-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=2)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=2)),
                ('size', models.DecimalField(decimal_places=3, max_digits=3)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(verbose_name=False)),
                ('buyer', models.ManyToManyField(related_name='games', to='task1.buyer')),
            ],
        ),
    ]
