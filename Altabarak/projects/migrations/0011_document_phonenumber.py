# Generated by Django 2.0.6 on 2018-09-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_document_empemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
