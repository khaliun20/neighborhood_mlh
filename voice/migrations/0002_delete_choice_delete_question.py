# Generated by Django 4.1.5 on 2023-05-19 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]