# Generated by Django 2.1.3 on 2018-11-17 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kencleng_core', '0003_auto_20181116_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transksi',
            old_name='deskripsi',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='transksi',
            old_name='jumlah',
            new_name='b',
        ),
        migrations.RenameField(
            model_name='transksi',
            old_name='dibuat',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='transksi',
            old_name='diubah',
            new_name='d',
        ),
        migrations.RenameField(
            model_name='transksi',
            old_name='prmilik',
            new_name='e',
        ),
    ]
