# Generated by Django 3.1.7 on 2021-04-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20210407_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stroka',
            name='create_at',
            field=models.DateTimeField(verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='stroka',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
