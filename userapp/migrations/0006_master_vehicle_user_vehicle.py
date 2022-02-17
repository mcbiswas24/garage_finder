# Generated by Django 2.0 on 2020-02-09 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0028_auto_20200209_1336'),
        ('userapp', '0005_auto_20200207_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master_Vehicle',
            fields=[
                ('Vimage', models.ImageField(default='abc.jpg', upload_to='image/')),
                ('Vname', models.CharField(max_length=20)),
                ('Vmodel', models.CharField(max_length=20)),
                ('Vtype', models.CharField(max_length=20)),
                ('Vnumber', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Vcolor', models.CharField(max_length=20)),
                ('User_ID', models.ForeignKey(default='abc@gmail.com', on_delete=django.db.models.deletion.CASCADE, to='authapp.Master_Table')),
            ],
        ),
        migrations.CreateModel(
            name='User_Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vimage', models.ImageField(default='abc.jpg', upload_to='image/')),
                ('Vname', models.CharField(max_length=20)),
                ('Vmodel', models.CharField(max_length=20)),
                ('Vtype', models.CharField(max_length=20)),
                ('Vcolor', models.CharField(max_length=20)),
                ('Vnumber', models.CharField(max_length=20)),
                ('Vehicle_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='userapp.Master_Vehicle')),
            ],
        ),
    ]