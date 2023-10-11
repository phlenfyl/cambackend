# Generated by Django 4.2.4 on 2023-09-28 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sermon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='sermon.author'),
        ),
    ]
