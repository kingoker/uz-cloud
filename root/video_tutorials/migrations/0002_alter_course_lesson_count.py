# Generated by Django 4.2 on 2023-05-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lesson_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
