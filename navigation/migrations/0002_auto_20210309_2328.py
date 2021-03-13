# Generated by Django 3.1.6 on 2021-03-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cathedra',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='cathedra_logos/', verbose_name='Логотип кафедры'),
        ),
        migrations.AddField(
            model_name='cathedra',
            name='info',
            field=models.TextField(default=None, max_length=500, verbose_name='Описание кафедры'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='faculty_logos/', verbose_name='Логотип факультета'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='info',
            field=models.TextField(default=None, max_length=500, verbose_name='Описание факультета'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.png', upload_to='avatars/', verbose_name='Фотография преподавателя'),
        ),
    ]
