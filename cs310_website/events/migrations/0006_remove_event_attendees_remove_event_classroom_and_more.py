# Generated by Django 4.0 on 2022-01-29 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rename_first_name_myclassstudent_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
        migrations.RemoveField(
            model_name='event',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='teacher',
        ),
    ]
