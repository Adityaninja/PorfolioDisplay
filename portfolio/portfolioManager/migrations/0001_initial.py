# Generated by Django 2.0.7 on 2018-07-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]
