# Generated by Django 2.2 on 2020-03-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_title',
            field=models.CharField(default='Title', max_length=50),
        ),
    ]
