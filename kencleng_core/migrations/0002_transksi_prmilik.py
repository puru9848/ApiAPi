# Generated by Django 2.1.3 on 2018-11-16 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kencleng_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transksi',
            name='prmilik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
