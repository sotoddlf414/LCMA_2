# Generated by Django 3.0.2 on 2020-02-21 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200221_0008'),
        ('maintenance', '0005_breakfix_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Greasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grease_type', models.CharField(default='G10', max_length=30)),
                ('grease_pcs', models.IntegerField(default=0)),
                ('grease_expire', models.DateField()),
                ('grease_supply', models.CharField(max_length=20)),
                ('grease_condition', models.CharField(max_length=20)),
                ('index_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.index')),
            ],
        ),
    ]