# Generated by Django 2.1.5 on 2021-04-24 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0003_delete_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furnitures',
            name='description',
        ),
        migrations.RemoveField(
            model_name='furnitures',
            name='price',
        ),
    ]
