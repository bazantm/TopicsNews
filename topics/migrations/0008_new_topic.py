# Generated by Django 4.1.2 on 2022-10-13 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('topics', '0007_rename_news_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.topic'),
        ),
    ]
