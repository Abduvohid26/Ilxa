# Generated by Django 5.0 on 2024-01-15 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='password_confirmation',
            field=models.CharField(max_length=128),
        ),
    ]
