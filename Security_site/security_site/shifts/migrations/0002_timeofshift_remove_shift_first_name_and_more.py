# Generated by Django 4.1.7 on 2023-03-26 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeOfShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='shift',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='last_name',
        ),
        migrations.AddField(
            model_name='shift',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shift',
            name='time_of_shift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shifts.timeofshift'),
        ),
    ]
