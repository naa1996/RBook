# Generated by Django 3.1.7 on 2021-04-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0011_auto_20210410_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalization',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
