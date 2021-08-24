# Generated by Django 3.2.4 on 2021-07-20 18:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('head_img', models.ImageField(upload_to='')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
