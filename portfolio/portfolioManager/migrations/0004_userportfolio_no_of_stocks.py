# Generated by Django 2.0.7 on 2018-07-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioManager', '0003_auto_20180728_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='userportfolio',
            name='no_of_stocks',
            field=models.BigIntegerField(default=0),
        ),
    ]