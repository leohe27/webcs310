# Generated by Django 4.0 on 2022-02-15 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_myclassstudent_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myclassstudent',
            old_name='teacher',
            new_name='lecturer',
        ),
    ]
