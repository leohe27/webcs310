# Generated by Django 4.0 on 2022-02-15 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_delete_myclassstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClassStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('badge', models.CharField(blank=True, max_length=30, null=True)),
                ('teacher', models.CharField(max_length=60)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.classroom')),
            ],
        ),
    ]
