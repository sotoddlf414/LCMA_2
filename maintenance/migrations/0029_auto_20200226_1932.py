# Generated by Django 3.0.2 on 2020-02-26 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0028_remove_breakfix_hour_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='etc',
            name='checked_ECT',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='etc',
            name='checked_MRT',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='etc',
            name='checked_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
