# Generated by Django 4.1.7 on 2023-03-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('plot', models.CharField(max_length=100)),
                ('poster', models.CharField(max_length=100)),
                ('imdb_id', models.CharField(max_length=100)),
            ],
        ),
    ]
