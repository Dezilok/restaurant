# Generated by Django 3.1.11 on 2021-05-29 17:02

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=60, verbose_name='Name of food')),
                ('image', models.ImageField(upload_to='images/food/', verbose_name='Image of food')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price of food')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Food Address')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('foodType', models.CharField(choices=[('meal', 'Meal'), ('dessert', 'Dessert'), ('drink', 'Drink')], max_length=20, verbose_name='Type of food')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
