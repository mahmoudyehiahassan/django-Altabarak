# Generated by Django 2.0.6 on 2018-08-21 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_senddata_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senddata',
            name='upload',
        ),
    ]
