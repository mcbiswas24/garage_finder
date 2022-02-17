# Generated by Django 2.0 on 2020-02-07 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20200207_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_provider',
            name='SP_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.Master_Table'),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.Master_Table'),
        ),
    ]
