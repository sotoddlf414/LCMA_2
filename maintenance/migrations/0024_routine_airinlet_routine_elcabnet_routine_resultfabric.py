# Generated by Django 3.0.2 on 2020-02-25 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200221_0008'),
        ('maintenance', '0023_routine_bristle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine_resultfabric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('checked_ECT', models.IntegerField(default=0)),
                ('checked_MRT', models.IntegerField(default=0)),
                ('result_Comment', models.TextField()),
                ('result_surface', models.BooleanField(default=True)),
                ('result_notch', models.BooleanField(default=True)),
                ('result_inangle', models.BooleanField(default=True)),
                ('result_outangle', models.BooleanField(default=True)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Routine_elcabnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('checked_ECT', models.IntegerField(default=0)),
                ('checked_MRT', models.IntegerField(default=0)),
                ('elec_Comment', models.TextField()),
                ('elec_board', models.BooleanField(default=True)),
                ('elec_Cable', models.BooleanField(default=True)),
                ('elec_4axis', models.BooleanField(default=True)),
                ('elec_cleaning', models.BooleanField(default=True)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Routine_airinlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('checked_ECT', models.IntegerField(default=0)),
                ('checked_MRT', models.IntegerField(default=0)),
                ('airinlet_Comment', models.TextField()),
                ('airinlet_Regulator', models.BooleanField(default=True)),
                ('airinlet_Separator', models.BooleanField(default=True)),
                ('airinlet_setting', models.BooleanField(default=True)),
                ('airinlet_pressure', models.BooleanField(default=True)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
    ]