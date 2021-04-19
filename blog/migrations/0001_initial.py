# Generated by Django 3.2 on 2021-04-18 10:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0002_auto_20210324_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Человечиские url')),
                ('title', models.CharField(max_length=20, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип статьи',
                'verbose_name_plural': 'Типы статей',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тег')),
                ('date', models.DateField(verbose_name='Дата')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person', verbose_name='Aвтор')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование')),
                ('text', models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(10, message='Текст статьи должен быть не короче 10 символов')], verbose_name='Текст статьи')),
                ('date', models.DateField(verbose_name='Дата')),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person', verbose_name='Aвтор')),
                ('tag_id', models.ManyToManyField(blank=True, null=True, to='blog.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['title'],
            },
        ),
    ]
