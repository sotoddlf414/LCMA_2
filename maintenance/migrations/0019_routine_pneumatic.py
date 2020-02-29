# Generated by Django 3.0.2 on 2020-02-25 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200221_0008'),
        ('maintenance', '0018_routine_rotationblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine_pneumatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField()),
                ('checked_ECT', models.IntegerField(default=0)),
                ('checked_MRT', models.IntegerField(default=0)),
                ('pneumatic_Comment', models.TextField()),
                ('pneumatic_hose', models.BooleanField(default=True)),
                ('pneumatic_bladeCylinder', models.BooleanField(default=True)),
                ('pneumatic_pressfootcylinder', models.BooleanField(default=True)),
                ('pneumatic_Drill', models.BooleanField(default=True)),
                ('pneumatic_Sharpning', models.BooleanField(default=True)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
    ]