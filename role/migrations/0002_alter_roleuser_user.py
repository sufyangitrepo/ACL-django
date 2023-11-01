# Generated by Django 4.2.6 on 2023-10-27 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_user', to=settings.AUTH_USER_MODEL),
        ),
    ]