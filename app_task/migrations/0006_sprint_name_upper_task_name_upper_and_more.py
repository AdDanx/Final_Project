# Generated by Django 4.1.5 on 2023-03-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_task', '0005_alter_proj_name_upper'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='name_upper',
            field=models.CharField(default='', help_text='Название спринта в ВЕРХНЕМ регистре', max_length=120, verbose_name='НАЗВАНИЕ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='name_upper',
            field=models.CharField(default=' ', help_text='Название задачи в ВЕРХНЕМ регистре', max_length=120, verbose_name='НАЗВАНИЕ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proj',
            name='name_upper',
            field=models.CharField(help_text='Название проекта в ВЕРХНЕМ регистре', max_length=120, verbose_name='НАЗВАНИЕ'),
        ),
    ]