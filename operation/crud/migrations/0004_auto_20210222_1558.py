# Generated by Django 2.1.5 on 2021-02-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210222_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mob',
            field=models.IntegerField(),
        ),
    ]
