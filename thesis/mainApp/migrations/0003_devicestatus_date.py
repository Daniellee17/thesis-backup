# Generated by Django 3.0.2 on 2020-01-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20200109_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicestatus',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]