# Generated by Django 2.0.3 on 2018-03-31 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panchayat',
            name='dev_index',
        ),
    ]