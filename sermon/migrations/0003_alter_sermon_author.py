# Generated by Django 4.1.4 on 2023-10-03 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sermon', '0002_alter_sermon_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sermon.author'),
        ),
    ]
