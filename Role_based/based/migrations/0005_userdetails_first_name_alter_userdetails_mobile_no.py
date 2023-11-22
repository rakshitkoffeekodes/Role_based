# Generated by Django 4.2.2 on 2023-11-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('based', '0004_alter_userdetails_mobile_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='mobile_no',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
