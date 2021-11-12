# Generated by Django 3.2.4 on 2021-11-12 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
