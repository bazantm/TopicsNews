# Generated by Django 4.1.2 on 2022-10-13 19:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('topics', '0009_alter_topic_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='text',
        ),
    ]
