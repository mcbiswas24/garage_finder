# Generated by Django 2.0 on 2020-01-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20200112_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_table',
            name='Role',
            field=models.CharField(max_length=50),
        ),
    ]