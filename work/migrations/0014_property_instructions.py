# Generated by Django 2.0.2 on 2018-10-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0013_auto_20181007_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='instructions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
