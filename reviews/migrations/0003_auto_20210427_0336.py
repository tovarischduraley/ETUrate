# Generated by Django 3.1.6 on 2021-04-27 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210427_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cathedrareview',
            name='attitude_to_student_mark',
            field=models.IntegerField(default=0, verbose_name='Отношение к студентам'),
        ),
        migrations.AlterField(
            model_name='cathedrareview',
            name='availability_of_cathedra_internship_mark',
            field=models.IntegerField(default=0, verbose_name='Возможность стажировки на кафедре'),
        ),
        migrations.AlterField(
            model_name='cathedrareview',
            name='find_job_opportunity_mark',
            field=models.IntegerField(default=0, verbose_name='Возможность найти работу'),
        ),
        migrations.AlterField(
            model_name='cathedrareview',
            name='relevance_of_material_mark',
            field=models.IntegerField(default=0, verbose_name='Современность материала'),
        ),
        migrations.AlterField(
            model_name='lecturereview',
            name='communicability_mark',
            field=models.IntegerField(default=0, verbose_name='Связь с аудиторией'),
        ),
        migrations.AlterField(
            model_name='lecturereview',
            name='knowledge_mark',
            field=models.IntegerField(default=0, verbose_name='Объём знаний по предмету'),
        ),
        migrations.AlterField(
            model_name='lecturereview',
            name='objectivity_mark',
            field=models.IntegerField(default=0, verbose_name='Объективность оценивания'),
        ),
        migrations.AlterField(
            model_name='lecturereview',
            name='teacher_talent_mark',
            field=models.IntegerField(default=0, verbose_name='Умение дать материал'),
        ),
        migrations.AlterField(
            model_name='practicereview',
            name='communicability_mark',
            field=models.IntegerField(default=0, verbose_name='Связь с аудиторией'),
        ),
        migrations.AlterField(
            model_name='practicereview',
            name='knowledge_mark',
            field=models.IntegerField(default=0, verbose_name='Объём знаний по предмету'),
        ),
        migrations.AlterField(
            model_name='practicereview',
            name='load_mark',
            field=models.IntegerField(default=0, verbose_name='Требовательность'),
        ),
        migrations.AlterField(
            model_name='practicereview',
            name='objectivity_mark',
            field=models.IntegerField(default=0, verbose_name='Объективность оценивания'),
        ),
    ]
