# Generated by Django 3.1.6 on 2021-03-13 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0007_auto_20210313_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='cathedra',
            new_name='cathedras',
        ),
    ]
