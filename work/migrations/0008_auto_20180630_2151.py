# Generated by Django 2.0.2 on 2018-07-01 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_auto_20180630_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='route',
            name='route_location',
        ),
        migrations.AddField(
            model_name='routejob',
            name='job_route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_route', to='work.Route'),
        ),
        migrations.AddField(
            model_name='routejob',
            name='route_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='route_location', to='work.Property'),
        ),
    ]
