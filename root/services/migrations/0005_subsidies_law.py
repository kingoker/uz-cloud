# Generated by Django 4.2.2 on 2023-08-10 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_partnership_alter_certificate_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsidies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Субсидия на')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Субсидия',
                'verbose_name_plural': 'Субсидии',
            },
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Номер указа')),
                ('about', models.CharField(max_length=255, verbose_name='Название указа')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('subsidy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.subsidies', verbose_name='Субсидия')),
            ],
            options={
                'verbose_name': 'Закон',
                'verbose_name_plural': 'Законы',
            },
        ),
    ]
