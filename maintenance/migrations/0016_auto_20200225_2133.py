# Generated by Django 3.0.2 on 2020-02-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0015_routine_sharpningarm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routine_sharpningarm',
            old_name='cleaning_condition',
            new_name='Sharpning',
        ),
        migrations.RenameField(
            model_name='routine_sharpningarm',
            old_name='fixed_condition',
            new_name='Sharpning_Arm',
        ),
        migrations.RenameField(
            model_name='routine_sharpningarm',
            old_name='plate_condition',
            new_name='Sharpning_Pully',
        ),
        migrations.RenameField(
            model_name='routine_sharpningarm',
            old_name='roller_condition',
            new_name='Sharpning_wire',
        ),
        migrations.AddField(
            model_name='routine_sharpningarm',
            name='sharpning_Cleaning',
            field=models.BooleanField(default=True),
        ),
    ]
