# Generated by Django 4.0 on 2022-02-15 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_rename_teacher_myclassstudent_lecturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myclassstudent',
            name='lecturer',
        ),
    ]