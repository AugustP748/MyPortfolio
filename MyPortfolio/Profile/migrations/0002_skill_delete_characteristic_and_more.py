# Generated by Django 4.2 on 2023-11-15 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_name', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('visible', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.DeleteModel(
            name='Characteristic',
        ),
        migrations.DeleteModel(
            name='TypeCharacteristic',
        ),
    ]
