# Generated by Django 3.1.4 on 2021-05-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='url',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]