# Generated by Django 3.0.2 on 2020-02-25 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200221_0008'),
        ('maintenance', '0012_routine_pressfoot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine_bladeguide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('comment', models.TextField()),
                ('plate_condition', models.BooleanField(default=True)),
                ('roller_condition', models.BooleanField(default=True)),
                ('fixed_condition', models.BooleanField(default=True)),
                ('cleaning_condition', models.BooleanField(default=True)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
    ]