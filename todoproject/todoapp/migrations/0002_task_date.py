# Generated by Django 4.2.8 on 2023-12-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-12-12'),
            preserve_default=False,
        ),
    ]
