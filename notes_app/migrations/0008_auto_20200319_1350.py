# Generated by Django 2.2 on 2020-03-19 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0007_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_text',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='note',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]