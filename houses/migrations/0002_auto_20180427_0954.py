# Generated by Django 2.0.2 on 2018-04-27 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'type', 'verbose_name_plural': 'categories'},
        ),
    ]
