# Generated by Django 4.1.7 on 2023-03-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0004_rename_afternoon_timeofshift_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeofshift',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='data_time',
            field=models.DateField(null=True),
        ),
    ]
