# Generated by Django 4.0.4 on 2022-11-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-11-19'),
            preserve_default=False,
        ),
    ]
