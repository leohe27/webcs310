# Generated by Django 4.0 on 2022-02-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_alter_event_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lesson',
            field=models.CharField(max_length=30, verbose_name='Lesson Name'),
        ),
    ]
