# Generated by Django 5.0.4 on 2024-05-29 11:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_alter_serv_info_lasting_alter_serv_info_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='login',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='password',
        ),
        migrations.AddField(
            model_name='clients',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='auth.user', verbose_name='Пользователь'),
        preserve_default=False,
        ),
    ]
