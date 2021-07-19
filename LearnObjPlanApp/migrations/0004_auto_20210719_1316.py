# Generated by Django 3.2.5 on 2021-07-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnObjPlanApp', '0003_auto_20210719_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='origin',
            name='origin',
            field=models.CharField(help_text='Where did this requirement come from? Common sources are syllabi, accreditors, or institutional objectives. Leave blank for children.', max_length=200),
        ),
    ]
