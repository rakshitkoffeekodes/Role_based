# Generated by Django 4.2.2 on 2023-11-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('based', '0008_alter_userdetails_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='mobile_no',
            field=models.SmallIntegerField(),
        ),
    ]
