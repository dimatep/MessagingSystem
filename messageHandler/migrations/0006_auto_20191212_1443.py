# Generated by Django 3.0 on 2019-12-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageHandler', '0005_auto_20191212_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]