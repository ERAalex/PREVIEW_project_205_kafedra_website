# Generated by Django 4.0.3 on 2022-12-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article_main',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('text', models.TextField(max_length=50, verbose_name='описание')),
                ('show_item', models.BooleanField(default=False, verbose_name='Отобразить')),
            ],
            options={
                'verbose_name': 'Главная страница - статьи',
                'verbose_name_plural': 'Главная страница - статьи',
            },
        ),
    ]