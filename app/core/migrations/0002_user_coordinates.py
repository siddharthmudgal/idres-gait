# Generated by Django 3.2 on 2021-04-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coordinates',
            field=models.TextField(default='NA', max_length=255),
        ),
    ]
