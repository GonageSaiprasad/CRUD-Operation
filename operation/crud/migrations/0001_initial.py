# Generated by Django 2.1.5 on 2021-02-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=10)),
                ('confirmpassword', models.CharField(max_length=10)),
                ('mob', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('skill', models.CharField(max_length=10)),
            ],
        ),
    ]
