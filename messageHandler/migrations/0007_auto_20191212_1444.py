# Generated by Django 3.0 on 2019-12-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageHandler', '0006_auto_20191212_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
