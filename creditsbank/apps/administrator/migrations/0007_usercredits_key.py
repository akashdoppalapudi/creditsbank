# Generated by Django 3.1.4 on 2021-01-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_auto_20210112_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercredits',
            name='key',
            field=models.CharField(default='', max_length=200),
        ),
    ]
