# Generated by Django 3.1.4 on 2021-01-13 10:17

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_usercredits_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercredits',
            name='credits',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='', max_length=200)),
        ),
        migrations.AlterField(
            model_name='usercredits',
            name='key',
            field=django_cryptography.fields.encrypt(models.CharField(default='', max_length=200)),
        ),
    ]
