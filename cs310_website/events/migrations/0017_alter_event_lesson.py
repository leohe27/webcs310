# Generated by Django 4.0 on 2022-02-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_alter_event_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lesson',
            field=models.CharField(max_length=30),
        ),
    ]
