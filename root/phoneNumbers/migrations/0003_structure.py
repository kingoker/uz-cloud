# Generated by Django 4.2 on 2023-05-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneNumbers', '0002_department_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='structure/')),
            ],
        ),
    ]