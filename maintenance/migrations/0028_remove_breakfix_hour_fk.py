# Generated by Django 3.0.2 on 2020-02-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0027_auto_20200226_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breakfix',
            name='hour_fk',
        ),
    ]
