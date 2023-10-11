# Generated by Django 4.2.4 on 2023-09-12 13:05

import ckeditor.fields
from django.db import migrations, models
import embed_video.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='0.0.0.0', max_length=40, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, default='', null=True, upload_to='program')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('like_count', models.BigIntegerField(blank=True, default=0, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('like', models.ManyToManyField(blank=True, related_name='likes', to='program.address')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Program',
            },
        ),
    ]
