# Generated by Django 4.1.4 on 2023-10-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0009_remove_program_speical_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='speicalprogram',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
