# Generated by Django 4.2.6 on 2023-10-27 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('disabled', models.BooleanField(default=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permission.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='role.role')),
            ],
        ),
    ]
