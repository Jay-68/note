# Generated by Django 2.2 on 2020-03-19 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0005_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]