# Generated by Django 4.2 on 2023-07-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='learned',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]
