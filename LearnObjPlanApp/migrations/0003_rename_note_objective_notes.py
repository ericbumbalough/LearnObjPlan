# Generated by Django 3.2.5 on 2021-09-02 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearnObjPlanApp', '0002_auto_20210902_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objective',
            old_name='note',
            new_name='notes',
        ),
    ]
