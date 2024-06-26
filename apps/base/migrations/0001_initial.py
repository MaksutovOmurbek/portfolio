# Generated by Django 5.0.6 on 2024-05-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('info', models.TextField(verbose_name='Инфо о себе')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
