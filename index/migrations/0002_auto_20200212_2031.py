# Generated by Django 3.0.2 on 2020-02-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='running_hour',
            new_name='running_ECT',
        ),
        migrations.AddField(
            model_name='index',
            name='running_VMT',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
