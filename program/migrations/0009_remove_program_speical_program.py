# Generated by Django 4.1.4 on 2023-10-07 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0008_program_counseling_program_deliverance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='speical_program',
        ),
    ]
