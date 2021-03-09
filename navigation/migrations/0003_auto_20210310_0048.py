# Generated by Django 3.1.6 on 2021-03-09 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20210309_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.AlterField(
            model_name='cathedra',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cathedras', to='navigation.faculty', verbose_name='Факультет'),
        ),
        migrations.AlterField(
            model_name='cathedra',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка на кафедру'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка на факультет'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
