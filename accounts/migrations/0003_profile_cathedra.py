# Generated by Django 3.1.6 on 2021-03-24 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20210320_1424'),
        ('accounts', '0002_auto_20210320_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cathedra',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='navigation.cathedra'),
        ),
    ]