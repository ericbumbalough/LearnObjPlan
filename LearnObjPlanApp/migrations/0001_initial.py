# Generated by Django 3.2.5 on 2021-07-19 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective_text', models.TextField()),
                ('source_number', models.CharField(max_length=200)),
                ('note', models.TextField()),
                ('content_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnObjPlanApp.contentarea')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnObjPlanApp.course')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnObjPlanApp.origin')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnObjPlanApp.objective')),
            ],
        ),
        migrations.AddField(
            model_name='contentarea',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnObjPlanApp.course'),
        ),
        migrations.AddField(
            model_name='contentarea',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnObjPlanApp.origin'),
        ),
        migrations.AddField(
            model_name='contentarea',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnObjPlanApp.contentarea'),
        ),
    ]