# Generated by Django 4.2.2 on 2023-11-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('based', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='mobile_no',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
