# Generated by Django 3.0.2 on 2020-02-24 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200221_0008'),
        ('maintenance', '0009_injection_vig12'),
    ]

    operations = [
        migrations.CreateModel(
            name='Injection_yaxis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injection_point', models.CharField(max_length=100)),
                ('injection_date', models.DateField()),
                ('injection_ECT', models.IntegerField(default=0)),
                ('injection_MRT', models.IntegerField(default=0)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Injection_xaxis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injection_point', models.CharField(max_length=100)),
                ('injection_date', models.DateField()),
                ('injection_ECT', models.IntegerField(default=0)),
                ('injection_MRT', models.IntegerField(default=0)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Injection_vibrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injection_point', models.CharField(max_length=100)),
                ('injection_date', models.DateField()),
                ('injection_ECT', models.IntegerField(default=0)),
                ('injection_MRT', models.IntegerField(default=0)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Injection_vaccum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injection_point', models.CharField(max_length=100)),
                ('injection_date', models.DateField()),
                ('injection_ECT', models.IntegerField(default=0)),
                ('injection_MRT', models.IntegerField(default=0)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Injection_connecting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injection_point', models.CharField(max_length=100)),
                ('injection_date', models.DateField()),
                ('injection_ECT', models.IntegerField(default=0)),
                ('injection_MRT', models.IntegerField(default=0)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
        migrations.CreateModel(
            name='Injection_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
          
                ('comment', models.TextField()),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
    ]
