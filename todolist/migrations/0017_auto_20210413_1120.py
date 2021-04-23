# Generated by Django 3.1.7 on 2021-04-13 06:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0016_employee_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date',
        ),
        migrations.AddField(
            model_name='request',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]