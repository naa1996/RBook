# Generated by Django 3.1.7 on 2021-04-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_auto_20210410_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalization',
            name='date',
            field=models.DateTimeField(blank=True, verbose_name='Дата'),
        ),
    ]