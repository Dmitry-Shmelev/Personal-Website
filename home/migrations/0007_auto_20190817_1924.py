# Generated by Django 2.2.4 on 2019-08-17 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_latestproject_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latestproject',
            old_name='url',
            new_name='project_URL',
        ),
    ]
