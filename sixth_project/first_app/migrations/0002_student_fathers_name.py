# Generated by Django 5.1.7 on 2025-03-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fathers_name',
            field=models.TextField(default='Rahim'),
        ),
    ]
