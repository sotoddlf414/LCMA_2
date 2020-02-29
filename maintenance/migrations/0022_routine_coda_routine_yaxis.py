# Generated by Django 3.0.2 on 2020-02-25 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200221_0008'),
        ('maintenance', '0021_routine_xaxis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine_yaxis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('checked_ECT', models.IntegerField(default=0)),
                ('checked_MRT', models.IntegerField(default=0)),
                ('yaxis_Comment', models.TextField()),
                ('yaxis_rail', models.BooleanField(default=True)),
                ('yaxis_Cleaning', models.BooleanField(default=True)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Routine_coda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('checked_ECT', models.IntegerField(default=0)),
                ('checked_MRT', models.IntegerField(default=0)),
                ('coda_Comment', models.TextField()),
                ('coda_belt', models.BooleanField(default=True)),
                ('coda_consol', models.BooleanField(default=True)),
                ('coda_moving', models.BooleanField(default=True)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
    ]