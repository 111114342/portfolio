# Generated by Django 3.1.1 on 2020-11-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201108_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
