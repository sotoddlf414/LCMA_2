# Generated by Django 3.0.2 on 2020-02-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0013_routine_bladeguide'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine_bladeguide',
            name='checked_ECT',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='routine_bladeguide',
            name='checked_MRT',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='routine_pressfoot',
            name='checked_ECT',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='routine_pressfoot',
            name='checked_MRT',
            field=models.IntegerField(default=0),
        ),
    ]