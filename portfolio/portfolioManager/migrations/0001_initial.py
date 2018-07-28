# Generated by Django 2.0.7 on 2018-07-28 08:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_name', models.CharField(max_length=10)),
                ('stock_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_time', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_stocks', models.BigIntegerField(default=10)),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioManager.Stocks')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
