# Generated by Django 4.0.5 on 2022-08-08 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkup', '0006_alter_postjobmodel_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
