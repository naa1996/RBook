# Generated by Django 3.1.7 on 2021-04-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_formalization_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalization',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
    ]
