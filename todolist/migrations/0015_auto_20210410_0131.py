# Generated by Django 3.1.7 on 2021-04-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0014_auto_20210410_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalization',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
